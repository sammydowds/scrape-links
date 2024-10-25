from pathlib import Path
from bs4 import BeautifulSoup, SoupStrainer
import csv
from dotenv import load_dotenv
from urllib.parse import urlparse

import scrapy
import os 

load_dotenv()

IGNORE_DOMAINS = os.getenv('IGNORE_DOMAINS')

class LinkSpider(scrapy.Spider):
    name = "links"

    def __init__(self, urls=None, *args, **kwargs):
        super(LinkSpider, self).__init__(*args, **kwargs)
        env_urls = os.getenv('URLS')
        self.urls = (urls.split(',') if urls else []) or (env_urls.split(',') if env_urls else [])

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        soup = BeautifulSoup(response.body, 'html.parser')
        links = soup.find_all("a", href=True)
        internal_routes = []
        external_domains = []

        for link in links:
            parsedLink = urlparse(link["href"])
            if parsedLink.netloc in response.url or "https" not in link["href"]:
                if parsedLink.path and parsedLink.path not in internal_routes:
                    internal_routes.append(parsedLink.path)
            else:
                if parsedLink.netloc not in IGNORE_DOMAINS and parsedLink.netloc not in external_domains:
                    external_domains.append(parsedLink.netloc)

        # save internal links csv 
        csv_filename = f"./results/{response.url.split('//')[-1].replace('/', '_')}_internal.csv"
        with open(csv_filename, mode='w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            for routes in internal_routes:
                writer.writerow([routes])

        # save external links csv 
        csv_filename = f"./results/{response.url.split('//')[-1].replace('/', '_')}_external.csv"
        with open(csv_filename, mode='w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            for domain in external_domains:
                writer.writerow([domain])
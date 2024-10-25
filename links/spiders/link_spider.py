from pathlib import Path
from bs4 import BeautifulSoup, SoupStrainer
import csv
from dotenv import load_dotenv

import scrapy
import os 

load_dotenv()

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
        internal_links = []
        external_links = []

        for link in links:
            if response.url in link["href"] or link["href"] in response.url:
                internal_links.append(link["href"])
            else:
                external_links.append(link["href"])

        # save internal links csv 
        csv_filename = f"./results/{response.url.split('//')[-1].replace('/', '_')}_internal.csv"
        with open(csv_filename, mode='w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            for link in internal_links:
                writer.writerow([link])

        # save external links csv 
        csv_filename = f"./results/{response.url.split('//')[-1].replace('/', '_')}_external.csv"
        with open(csv_filename, mode='w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            for link in external_links:
                writer.writerow([link])
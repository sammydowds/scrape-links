
# Scrape links

## Summary

This is a very simple tool to scrape a url and output internal and external references into two separate CSV's. 

## Running

Ensure you have `poetry` installed. 

```
poetry install && poetry run scrapy crawl links -a urls=<insert urls here>
```
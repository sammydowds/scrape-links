
# Scrape links

## Summary

This is a very simple tool to scrape a url and output internal and external references into two separate CSV's. 

## Install dependencies

Ensure you have `poetry` installed. 

```
poetry install
```

## Scraping

Pass urls in command

```
poetry run scrapy crawl links -a urls=<insert urls here>
```

You can also pass through URLs via a `.env` file. 

```
// .env
URLS=...
```

to run

```
poetry run scrapy crawl links
```
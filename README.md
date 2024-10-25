
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

## Extras

You can also ignore domains with an environment var

```
// .env

IGNORE_DOMAINS=...
```

This will prevent common social media domains from being in the output muddying your analysis of unique and more interesting domains.

For example:
```
IGNORE_DOMAINS=truthsocial.com,rumble.com,twitter.com,www.facebook.com,www.tiktok.com,www.instagram.com,www.youtube.com,youtu.be,podcasts.apple.com,podcasts.google.com,open.spotify.com
```
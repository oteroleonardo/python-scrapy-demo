
Running the crawler
===================

```bash
> cd [PROJECT_FOLDER]/src
pip install -r requirements.txt
scrapy crawl stores_scraper -o stores_scraper.json -a partner=homedepot.com
```

Log level
============

Log level can be changed from

```bash
src/stores_scraper/settings.py
```

Where´s the scraping code
============

Scrapping code could be find into the spiders folder

```bash
src/stores_scraper/spiders/stores_scraper.py
```

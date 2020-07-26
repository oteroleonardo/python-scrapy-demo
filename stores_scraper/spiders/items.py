import scrapy
from scrapy.item import Item

class ParsedItems(Item):
    stores = scrapy.Field()
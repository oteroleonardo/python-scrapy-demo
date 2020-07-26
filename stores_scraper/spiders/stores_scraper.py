import os
import scrapy
import time
from .items import ParsedItems

if "stores_scraper.json" in os.listdir('./'):
    os.remove('./stores_scraper.json')

class StoresScraper(scrapy.Spider):
    name = "stores_scraper"
    def start_requests(self):
        yield scrapy.Request(url=f"https://givingassistant.org/coupon-codes/{self.partner}" , callback=self.parse, meta={'is_first_level': True, 'partner': self.partner})    

    def parse(self, response):
        partners = []
        parent_partner = response.meta['partner'] 
        print(f"parsing {parent_partner}")

        for href in response.xpath(
            '//*[@class="popular_stories"]/h3[contains(text(),"Similar Store Coupons")]/following-sibling::div//a/@href'
            ).extract():
            url = response.urljoin(href)
            partner = href.split('/')[-1]
            partners.append(partner)

            if(response.meta['is_first_level']) :
                yield scrapy.Request(url, callback=self.parse, meta={'is_first_level': False, 'partner': partner})
                time.sleep(0.001) #TODO It would be better configurable

        yield { parent_partner: partners}




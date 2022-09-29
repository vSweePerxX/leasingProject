import scrapy

from leasingNew.items import SixtItem
from datetime import datetime, date
from scrapy.crawler import CrawlerProcess

class SixtScraper(scrapy.Spider):
    name = 'sixtCrawler'
    start_urls = ['https://www.sixt-neuwagen.de/konfigurieren/audi?customerType=private',
                  'https://www.sixt-neuwagen.de/konfigurieren/bmw?customerType=private',
                  'https://www.sixt-neuwagen.de/konfigurieren/mercedes-benz?customerType=private']
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    today = date.today()
    print("Current Time =", current_time)

    custom_settings = {
        'FEEDS': { f'results/sixed_{today}_{current_time}.csv': { 'format': 'csv',}}
    }

    def parse(self, response):
        item = SixtItem()
        # for results in response.xpath('//li[@layout]'):
        liste = response.css('.vehicle-card')

        for auto in liste:
            item['Title'] = auto.css('.mb-1::text').get()
            item['Price'] = auto.css(".vehicle-card-offer-price span::text").get()
            item['TimeSpan'] = '48 Monate'
            item['Miles'] = 'Kilometerleasingvertrag mit Kaufoption'
            item['Picture'] = ''
            yield item
#run spider
process = CrawlerProcess()
process.crawl(SixtScraper)
process.start()
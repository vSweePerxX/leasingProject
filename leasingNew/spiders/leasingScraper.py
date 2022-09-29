import scrapy
from scrapy.crawler import CrawlerProcess
from selenium import webdriver
from selenium.webdriver.common.by import By

from leasingNew.items import leasingScraperItem
from leasingNew.items import SixtItem
from datetime import datetime, date



class LeasingScraper(scrapy.Spider):
    name = 'leasingCrawler'
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    today = date.today()
    print("Current Time =", current_time)

    custom_settings = {
        'FEEDS': { f'results/leasing_{today}_{current_time}.csv': { 'format': 'csv',}}
    }

    start_urls = ['https://www.leasingmarkt.de/listing?v=2&nc=1&mn=9&sort=popularity',
                  'https://www.leasingmarkt.de/listing?v=2&nc=1&mn=13&sort=popularity',
                  'https://www.leasingmarkt.de/listing?v=2&nc=1&mn=62&sort=popularity']

    def parse(self, response):
        item = leasingScraperItem()
        # for results in response.xpath('//li[@layout]'):
        liste = response.css(".shadow")

        for auto in liste:
            if auto.css(".overflow-ellipsis::text").get() is not None:
                item['Title'] = auto.css(".overflow-ellipsis::text").get().replace("\n","")
                item['Price'] = auto.css(".font-bold::text").get().replace(",00\xa0€","")
                item['TimeSpan'] = auto.css(".mb-1:nth-child(4) .text-black-100::text").get().replace("\n","")
                item['Miles'] = auto.css(".mb-1:nth-child(3) .text-black-100::text").get().replace("\n","")
                item['Picture'] = auto.css(".max-w-full .mobile\:w-full").attrib['src'].replace("/data","https://www.leasingmarkt.de/data")
                item['Link'] = auto.xpath('//a[@class="relative flex flex-row mobile:flex-col"]/@href').get()
                yield item

      #  for x in range(8):
      #      next_page_part = f'https://www.leasingmarkt.de/listing?v=2&nc=1&mn={gModel}&mlpt=300&sort=popularity&p={x}'

       #     if next_page_part is not None:
        #        yield scrapy.Request(next_page_part, callback=self.parse)

    #def parse_personPage(self, response):
       # item = leasingScraperItem()

        #item['Title'] = response.xpath('//div[@class="flex-inline text-3 text-turquoise-120 font-semibold whitespace-nowrap desktop:w-3/4 overflow-hidden truncate overflow-ellipsis"]/text()').get()

        #yield item
#run spider
process = CrawlerProcess()
process.crawl(LeasingScraper)
process.start()




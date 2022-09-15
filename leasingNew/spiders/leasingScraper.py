import scrapy
from selenium import webdriver
from selenium.webdriver.common.by import By

from leasingNew.items import leasingScraperItem


class LeasingScraper(scrapy.Spider):
    name = 'leasingCrawler'

    def __init__(self, model=''):
        global gModel
        gModel = model
        self.start_urls = [f'https://www.leasingmarkt.de/listing?v=2&nc=1&mn={model}&sort=popularity']
        #self.start_urls = ['https://www.leasingmarkt.de/listing?v=2&nc=1&mn=9&mlpt=300&sort=popularity']

    def parse(self, response):
        item = leasingScraperItem()
        # for results in response.xpath('//li[@layout]'):
        liste = response.css(".shadow")

        for auto in liste:
            if auto.css(".overflow-ellipsis::text").get() is not None:
                item['Title'] = auto.css(".overflow-ellipsis::text").get().replace("\n","")
                item['Price'] = auto.css(".font-bold::text").get().replace("\xa0€","€")
                item['TimeSpan'] = auto.css(".mb-1:nth-child(4) .text-black-100::text").get().replace("\n","")
                item['Miles'] = auto.css(".mb-1:nth-child(3) .text-black-100::text").get().replace("\n","")
                yield item

        for x in range(8):
            next_page_part = f'https://www.leasingmarkt.de/listing?v=2&nc=1&mn={gModel}&mlpt=300&sort=popularity&p={x}'

            if next_page_part is not None:
                yield scrapy.Request(next_page_part, callback=self.parse)

    #def parse_personPage(self, response):
       # item = leasingScraperItem()

        #item['Title'] = response.xpath('//div[@class="flex-inline text-3 text-turquoise-120 font-semibold whitespace-nowrap desktop:w-3/4 overflow-hidden truncate overflow-ellipsis"]/text()').get()

        #yield item

class MobileScraper(scrapy.Spider):
    name = 'mobileCrawler'
    start_urls = ['https://suchen.mobile.de/fahrzeuge/search.html?dam=0&isSearchRequest=true&ref=quickSearch&sb=rel&vc=Car']


    def parse(self, response):
        item = leasingScraperItem()
        # for results in response.xpath('//li[@layout]'):
        liste = response.css(".cBox--resultList > .cBox-body")

        for auto in liste:
            item['Title'] = auto.css(".u-text-break-word::text").get()
            yield item

       # for x in range(8):
        #    next_page_part = f'https://www.leasingmarkt.de/listing?v=2&nc=1&mn={gModel}&mlpt=300&sort=popularity&p={x}'

         #   if next_page_part is not None:
          #      yield scrapy.Request(next_page_part, callback=self.parse)




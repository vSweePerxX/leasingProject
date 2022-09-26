import scrapy
from selenium import webdriver
from selenium.webdriver.common.by import By

from leasingNew.items import leasingScraperItem


class LeasingScraper(scrapy.Spider):
    name = 'test'

    def start_requests(self, model=''):
        yield scrapy.Request(f'https://www.leasingmarkt.de/listing?v=2&nc=1&mn=9&sort=popularity',callback=self.parse1)
        yield scrapy.Request('url2',callback=self.parse2)

    def parse1(self, response):
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
                yield item

        for x in range(8):
            next_page_part = f'https://www.leasingmarkt.de/listing?v=2&nc=1&mn=9&mlpt=300&sort=popularity&p={x}'

            if next_page_part is not None:
                yield scrapy.Request(next_page_part, callback=self.parse1)

    def parse2(self, response):
        for url in response.css('.mr-directory-item a::attr(href)').getall():#loop for each href
            yield scrapy.Request(f'https://muckrack.com{url}', callback=self.parse_products,
                                 dont_filter=True)

    def parse_products(self, response):
        #these are for another website
        full_name = response.css('.mr-font-family-2.top-none::text').get()
        Media_outlet = response.css('.mr-person-job-item a::text').get()
        #yield {'header':'data'}
        yield {'Full Name': full_name, 'Media outlet':Media_outlet,'URL': response.url}
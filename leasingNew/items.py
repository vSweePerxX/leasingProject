# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class leasingScraperItem(scrapy.Item):
    # define the fields for your item here like:
    Title = scrapy.Field()
    Price = scrapy.Field()
    TimeSpan = scrapy.Field()
    Miles = scrapy.Field()
    Picture = scrapy.Field()
    Link = scrapy.Field()

class SixtItem(scrapy.Item):
    Title = scrapy.Field()
    Price = scrapy.Field()
    TimeSpan = scrapy.Field()
    Miles = scrapy.Field()
    Picture = scrapy.Field()



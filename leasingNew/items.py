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
class BvaiItem(scrapy.Item):

    name = scrapy.Field()
    adressPart1 = scrapy.Field()
    adressPart2 = scrapy.Field()
    partner = scrapy.Field()
    phone = scrapy.Field()
    mail = scrapy.Field()
    website = scrapy.Field()
    ManagingDirector_BoardMember = scrapy.Field()

class GelbeSeitenItem(scrapy.Item):

    name = scrapy.Field()
    #spezifikation = scrapy.Field()
    straße_Hausnummer = scrapy.Field()
    PLZ = scrapy.Field()
    Branche = scrapy.Field()
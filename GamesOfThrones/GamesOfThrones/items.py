# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GamesofthronesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Title=scrapy.Field()
    Vote=scrapy.Field()
    Created_at= scrapy.Field()
    Comments= scrapy.Field()

# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class InfoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    star = scrapy.Field()
    review_info = scrapy.Field()
    detail_info_link = scrapy.Field()
    type = scrapy.Field()
    now_price = scrapy.Field()
    old_price = scrapy.Field()

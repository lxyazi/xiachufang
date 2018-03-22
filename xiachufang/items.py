# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy



class XiachufangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    ings = scrapy.Field()


class XiachufangTpyeItem(scrapy.Item):
    cates_list_info = scrapy.Field()
    cates_list = scrapy.Field()
    cates_list_herf = scrapy.Field()

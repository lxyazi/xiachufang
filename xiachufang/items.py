# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


# 每道菜的信息
class XiachufangItem(scrapy.Item):
    title = scrapy.Field()
    ings = scrapy.Field()
    # TODO:图片资源

# 总分类信息
class XiachufangTpyeItem(scrapy.Item):
    cates_list_info = scrapy.Field()
    cates_list = scrapy.Field()
    cates_list_herf = scrapy.Field()

# 子分类信息
class TpyeInfoItem(scrapy.Item):
    # TODO
    pass

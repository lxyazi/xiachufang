# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


# 每道菜的信息
class XiachufangItem(scrapy.Item):
    # TODO 图片资源

    # 综合评分
    score = scrapy.Field()
    # 多少人做过这道菜
    people_number = scrapy.Field()
    # 描述
    description = scrapy.Field()
    # 用料
    recipe_ingredient = scrapy.Field()
    # 做法步骤
    step = scrapy.Field()
    # 小贴士
    tip = scrapy.Field()
    # 创建时间
    create_time = scrapy.Field()
    # 收藏人数
    collection_number = scrapy.Field()
    # URL
    href = scrapy.Field()
    # 7天内做过的人数
    bold_score = scrapy.Field()
    # 菜名
    title = scrapy.Field()
    # 分类信息
    type_title = scrapy.Field()

    # # 用户名称
    # author = scrapy.Field()
    #
    # # # 用户唯一ID
    # # inventor_id = scrapy.Field()
    #
    # #用户URL
    # inventor_url = scrapy.Field()

    # TODO：用户信息

# 总分类信息
class XiachufangTpyeItem(scrapy.Item):
    cates_list_info = scrapy.Field()
    cates_list = scrapy.Field()
    cates_list_href = scrapy.Field()

# 子分类信息
class TpyeInfoItem(scrapy.Item):
    # TODO
    pass





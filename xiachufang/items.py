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

    # 用户名称
    author = scrapy.Field()
    #
    # #用户URL
    # author_url = scrapy.Field()

    # # # 用户唯一ID
    # # inventor_id = scrapy.Field()
    #

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


class XiachufangAuthorItem(scrapy.Item):
    # 作者姓名
    author = scrapy.Field()

    # 作者网站url，可用作唯一id
    author_url = scrapy.Field()

    # 作者性别
    author_sex = scrapy.Field()

    # 作者地理位置
    author_location1 = scrapy.Field()
    author_location2 = scrapy.Field()

    #作者职业
    author_profession = scrapy.Field()

    # 作者加入时间
    author_time = scrapy.Field()

    # 作者关注列表
    author_follow = scrapy.Field()

    # 作者关注列表url
    author_follow_url = scrapy.Field()

    # 作者被关注列表
    author_be_followed = scrapy.Field()

    # 作者被关注列表url
    author_be_followed_url = scrapy.Field()
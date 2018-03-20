# -*- coding: utf-8 -*-
import scrapy
from xiachufang.items import XiachufangItem

class XiachufangSpiderSpider(scrapy.Spider):
    name = 'xiachufang_spider'
    allowed_domains = ['www.xiachufang.com']
    start_urls = ['https://www.xiachufang.com/recipe/101790129/']

    def parse(self, response):
        items = []
        ings_level = []
        node_list = response.xpath(".//body//div[@class='ings']/table")

        # title：菜名； ings：用料及程度
        for node in node_list:
            ings_name = node.xpath(".//td[@class='name']/a/text()").extract()
            ings_lvl = node.xpath(".//td[@class='unit']/text()").extract()

        print(ings_name)
        print(ings_lvl)
        # title = ((response.xpath(".//body//div[@class='pure-g']//h1[@class='page-title']/text()").extract())[0]).extract()\
        #
        # ings = zip(ings_name, ings_level)
        #
        # for value in ings:
        #     print(value)

        # print(title)
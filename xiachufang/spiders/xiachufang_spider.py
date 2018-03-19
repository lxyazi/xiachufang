# -*- coding: utf-8 -*-
import scrapy
from xiachufang.items import XiachufangItem

class XiachufangSpiderSpider(scrapy.Spider):
    name = 'xiachufang_spider'
    allowed_domains = ['www.xiachufang.com']
    start_urls = ['https://www.xiachufang.com/recipe/101790129/']

    def parse(self, response):
        node_list = response.xpath(".//body//div[@class='ings']/table")
        items = []
        for node in node_list:
            title = node.xpath(".//td[@class='name']/a/text()").extract()
            ings = node.xpath(".//td[@class='unit']/text()").extract()

            for i, j in zip(title, ings):
                print(i +":" + j.strip())

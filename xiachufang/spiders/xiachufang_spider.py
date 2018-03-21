# -*- coding: utf-8 -*-
import scrapy
from xiachufang.items import XiachufangItem
from xiachufang.items import XiachufangTpyeItem


class XiachufangtypeSpiderSpider(scrapy.Spider):
	name = 'xiachufang_spider'
	allowed_domains = ['xiachufang.com']
	start_urls = ['https://www.xiachufang.com/category/']

	def parse(self, response):
		node_list = response.xpath(".//div[@class='cates-list clearfix has-bottom-border pb20 mb20']")

		for node in node_list:
			xiachufangType = XiachufangTpyeItem()

			xiachufangType['cates_list_info'] = \
				node.xpath(".//div[@class='cates-list-info ml15 float-left']/h3/text()").extract()[0]
			xiachufangType['cates_list_first'] = node.xpath(
				".//div[@class='cates-list-all clearfix hidden']/h4/text() | .//div[@class='cates-list-all clearfix hidden']/h4/a/text()").extract()
			xiachufangType['cates_list_second'] = node.xpath(
				".//div[@class='cates-list-all clearfix hidden']/ul[@class=' has-bottom-border']/li/a/text()").extract()[
				0]

			print("------------test1------------------")
			print(node.xpath(".//div[@class='cates-list-info ml15 float-left']/h3/text()").extract())

			print(node.xpath(
				".//div[@class='cates-list-all clearfix hidden']/h4/text() | .//div[@class='cates-list-all clearfix hidden']/h4/a/text()").extract())

			print(node.xpath(
				".//div[@class='cates-list-all clearfix hidden']/ul[@class=' has-bottom-border']/li/a/text()").extract())
			print("------------test2------------------")

# -*- coding: utf-8 -*-
import scrapy
from xiachufang.items import XiachufangItem
from xiachufang.items import XiachufangTpyeItem


class XiachufangtypeSpiderSpider(scrapy.Spider):
	name = 'xiachufang_spider'
	allowed_domains = ['xiachufang.com']
	start_urls = ['https://www.xiachufang.com/category/']

	def parse(self, response):
		count = 0
		node_list_1 = response.xpath(".//div[@class='cates-list clearfix has-bottom-border pb20 mb20']")
		for node1 in node_list_1:
			cates_list_info = node1.xpath("./div[@class='cates-list-info ml15 float-left']/h3/text()").extract()[0]
			h4_cates_list = []
			h4_cates_list_herf = []
			node_list_h4 = node1.xpath(".//div[@class='cates-list-all clearfix hidden']/h4")

			print("------------test1------------------")
			print(len(node_list_h4))
			print("------------test2------------------")

			for node_h4 in node_list_h4:

				if len(node_h4.xpath("./a")) != 0:
					h4_cates_list.append(node_h4.xpath("./a/text()").extract()[0])
					h4_cates_list_herf.append(node_h4.xpath("./a/@href").extract()[0])
				else:
					h4_cates_list.append(" ")
					h4_cates_list_herf.append(" ")

			node_list_ul = node1.xpath(".//div[@class='cates-list-all clearfix hidden']/ul")
			i = 0
			for node_ul in node_list_ul:
				if len(node_ul.xpath("./li")) == 0:
					item = XiachufangTpyeItem()
					item['cates_list_info'] = cates_list_info
					item['cates_list'] = h4_cates_list[i]
					item['cates_list_herf'] = "https://www.xiachufang.com" + h4_cates_list_herf[i]
					yield item
					yield scrapy.Request(item['cates_list_herf'], meta={'cates_list_info': item['cates_list_info']},
					                     callback=self.listParse)
					# count += 1

					print("------------test1------------------")
					print(item['cates_list_info'])
					print(item['cates_list'])
					print(item['cates_list_herf'])
					print("------------test2------------------")

				else:
					for node_li in node_ul.xpath("./li"):
						item = XiachufangTpyeItem()
						item['cates_list_info'] = cates_list_info
						item['cates_list'] = node_li.xpath("./a/text()").extract()[0]
						item['cates_list_herf'] = "https://www.xiachufang.com" + node_li.xpath("./a/@href").extract()[0]
						yield item
						yield scrapy.Request(item['cates_list_herf'], meta={'cates_list_info': item['cates_list_info']},
						                     callback=self.listParse)
						# count += 1

						print("------------test1------------------")
						print(item['cates_list_info'])
						print(item['cates_list'])
						print(item['cates_list_herf'])
						print("------------test2------------------")

	def listParse(self, response):
		# TODO
		messageFromParse = response.meta
		pass

	def itemParse(self, response):
		# TODO
		pass

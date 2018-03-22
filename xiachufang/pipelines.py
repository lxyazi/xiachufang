# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
from xiachufang.items import XiachufangItem
from xiachufang.items import XiachufangTpyeItem


class XiachufangPipeline(object):
	def __init__(self):
		self.fileType = open("fileTpye.json", "w")

	def process_item(self, item, spider):
		if type(item) == XiachufangItem:
			pass

		if type(item) == XiachufangTpyeItem:
			print("数据已经过管道")
			content = json.dumps(dict(item), ensure_ascii=False) + ",\n"
			self.fileType.write(content)
			return item

	def close_sipder(self, spider):
		self.fileType.close()

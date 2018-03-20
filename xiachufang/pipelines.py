# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class XiachufangPipeline(object):
    def process_item(self, item, spider):
        if type(item) == XiachufangItem:
            pass

        if type(item) == XiachufangTpyeItem:
            pass

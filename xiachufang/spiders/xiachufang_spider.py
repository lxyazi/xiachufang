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
            h4_cates_list_href = []
            node_list_h4 = node1.xpath(".//div[@class='cates-list-all clearfix hidden']/h4")

            print("------------test1------------------")
            print(len(node_list_h4))
            print("------------test2------------------")

            for node_h4 in node_list_h4:

                if len(node_h4.xpath("./a")) != 0:
                    h4_cates_list.append(node_h4.xpath("./a/text()").extract()[0])
                    h4_cates_list_href.append(node_h4.xpath("./a/@href").extract()[0])
                else:
                    h4_cates_list.append(" ")
                    h4_cates_list_href.append(" ")

            node_list_ul = node1.xpath(".//div[@class='cates-list-all clearfix hidden']/ul")
            i = 0
            for node_ul in node_list_ul:

                # ul下的目录item
                if len(node_ul.xpath("./li")) == 0:
                    item = XiachufangTpyeItem()
                    item['cates_list_info'] = cates_list_info
                    item['cates_list'] = h4_cates_list[i]
                    item['cates_list_href'] = "https://www.xiachufang.com" + h4_cates_list_href[i]
                    yield item
                    yield scrapy.Request(item['cates_list_href'], callback=self.listParse)

                    # yield scrapy.Request(item['cates_list_href'], meta={'cates_list_info': item['cates_list_info']},
                    #                      callback=self.listParse)
                    # count += 1

                    # 输出结果，进行检验
                    print("------------test1------------------")
                    print(item['cates_list_info'])
                    print(item['cates_list'])
                    print(item['cates_list_href'])
                    print("------------test2------------------")

                # 若ul下无目录，则使用h4作为目录item
                else:
                    for node_li in node_ul.xpath("./li"):
                        item = XiachufangTpyeItem()
                        item['cates_list_info'] = cates_list_info
                        item['cates_list'] = node_li.xpath("./a/text()").extract()[0]
                        item['cates_list_href'] = "https://www.xiachufang.com" + node_li.xpath("./a/@href").extract()[0]
                        yield item
                        yield scrapy.Request(item['cates_list_href'], callback=self.listParse)

                        # yield scrapy.Request(item['cates_list_href'], meta={'cates_list_info': item['cates_list_info']},
                        #                      callback=self.listParsee)
                        # count += 1

                        # 输出结果，进行检验
                        print("------------test1------------------")
                        print(item['cates_list_info'])
                        print(item['cates_list'])
                        print(item['cates_list_href'])
                        print("------------test2------------------")

    def listParse(self, response):
        # 是否下一页
        indexNext = True

        # 提取分类标题
        title = response.xpath(".//div[@class='pure-g' or @class='pure-u align-middle']//h1/text()").extract()[0]

        # 遍历该页中的每一道菜
        node_list = response.xpath(".//div[@class='normal-recipe-list']//li")
        for node in node_list:
            url = "https://www.xiachufang.com" + node.xpath("./a/@href").extract()[0]
            if len(node.xpath(".//p[@class='stats']/span[@class='bold score']")) != 0:
                bold_score = node.xpath(".//p[@class='stats']/span[@class='bold score']/text()").extract()[0]
            else:
                bold_score = "0"
            yield scrapy.Request(url, meta={"bold_score": bold_score, "href": url, "typeTitle": title},
                                 callback=self.itemParse)

        # 下一页
        if len(node_list) == 0 or len(response.xpath(".//span[@class='next']")) == 1:
            indexNext = False
        if indexNext:
            yield scrapy.Request("https://www.xiachufang.com" +
                                 response.xpath(".//div[@class='pager']/a[@class='next']/@href").extract()[0],
                                 callback=self.listParse)

    def itemParse(self, response):
        # TODO

        # 创建时间  create_time   ----------
        # 收藏人数  collection_number   ----------
        # URL   herf   ----------
        # 7天内做过的人数  bold_score   ----------
        # 菜名    title   ----------
        # 分类信息  type_title   ----------
        # 综合评分  score   ----------
        # 多少人做过这道菜  people_number   ----------
        # 描述    description   ----------
        # 用料    recipe_ingredient   ----------
        # 做法步骤  step   ----------
        # 小贴士   tip   ----------

        item = XiachufangItem()

        item['title'] = (response.xpath(".//h1[@class='page-title']/text()").extract()[0]).strip()
        item['bold_score'] = response.meta['bold_score']
        item['href'] = response.meta['href']
        item['type_title'] = response.meta['typeTitle']
        item['collection_number'] = response.xpath(".//div[@class='pv']/text()").extract()[0]
        item['create_time'] = response.xpath(".//div[@class='time']/span/text()").extract()[0]

        # --------------------------------------------------------------------------------------------------------------------
        if len(response.xpath(".//div[@class='tip-container']/div[@class='tip']")) != 0:
            item['tip'] = (
            response.xpath(".//div[@class='tip-container']/div[@class='tip']/text()").extract()[0]).strip()
        else:
            item['tip'] = "无"
        # --------------------------------------------------------------------------------------------------------------------

        if len(response.xpath(".//div[@class='desc mt30']")) != 0:
            item['description'] = (response.xpath(".//div[@class='desc mt30']/text()").extract()[0]).strip()
        else:
            item['tip'] = "无"

        # --------------------------------------------------------------------------------------------------------------------
        if len(response.xpath(".//div[@class='score float-left']/span[@class='number']")) != 0:
            item['score'] = response.xpath(".//div[@class='score float-left']/span[@class='number']/text()").extract()[
                0]
        else:
            item['score'] = "-1"
        # --------------------------------------------------------------------------------------------------------------------

        item['people_number'] = \
            response.xpath(".//div[@class='cooked float-left']/span[@class='number']/text()").extract()[0]

        # item['recipe_ingredient'] = 'test'
        # item['step'] = 'test'

        # --------------------------------------------------------------------------------------------------------------------
        ingsNodeList = response.xpath(".//div[@class='ings']/table/tbody/tr[@itemprop='recipeIngredient']")
        # 用料
        ings1 = []
        ings2 = []
        for node in ingsNodeList:
            # 用料是否存在
            if len(node.xpath("./td[@class='name']")) == 0:
                ings1.append('略')
            else:
                ings1.append(node.xpath("./td[@class='name']/text()").extract()[0])

            # 用量是否存在
            if len(node.xpath("./td[@class='name']")) == 0:
                ings1.append('无')
            else:
                ings2.append(node.xpath("./td[@class='unit']/text()").extract()[0])

        ings = ""
        for (v1, v2) in zip(ings1, ings2):
            ings += " ## " + v1 + " *:* " + v2
        item['recipe_ingredient'] = ings
        # --------------------------------------------------------------------------------------------------------------------

        steps = ""
        for step in response.xpath(".//div[@class='steps']//li/p/text()").extract():
            steps += " * " + step
        item['step'] = steps
        # --------------------------------------------------------------------------------------------------------------------

        yield item

# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 小说名称
    name = scrapy.Field()
    # 小说链接
    url = scrapy.Field()
    # 小说id
    number = scrapy.Field()
    # 小说类型
    category = scrapy.Field()
    # 作者
    author = scrapy.Field()
    # 小说状态
    status = scrapy.Field()
    # 收藏数
    collect = scrapy.Field()
    # 小说字数
    novelNumber = scrapy.Field()
    # 最后更新时间
    lastUpTime = scrapy.Field()
    # 点击数
    click = scrapy.Field()
    # 推荐数
    push = scrapy.Field()

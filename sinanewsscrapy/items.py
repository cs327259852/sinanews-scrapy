# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


# 新浪新闻列表实体
class SinaNewsItem(scrapy.Item):
    name = scrapy.Field()
    href = scrapy.Field()


# 新浪新闻详情实体
class SinaNewsDetailItem(scrapy.Item):
    name = scrapy.Field()
    details = scrapy.Field()
    href = scrapy.Field()

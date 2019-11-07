import scrapy
from sinanewsscrapy.items import SinaNewsDetailItem,SinaNewsItem
import json


#  新浪新闻列表爬虫
class SinaNewsSpider(scrapy.Spider):
    name = 'sinanewsspider'
    allowed_domains = 'sina.com.cn'
    start_urls = ['https://www.sina.com.cn/']

    def parse(self, response):
        node_list = response.xpath('//div[@class="top_newslist"]/ul/li')
        item_list = []
        for node in node_list:
            news_item = SinaNewsItem()
            name = node.xpath('./a/text()').extract()
            href = node.xpath('./a/@href').extract()
            if len(name) == 0:
                continue
            else:
                num_of_news = len(name)
                for i in range(num_of_news):
                    news_item['name'] = name[i]
                    news_item['href'] = href[i]
                    yield news_item


# 新浪新闻详情爬虫
class SinaNewsDetailSpider(scrapy.Spider):
    name = 'sinanewsdetailspider'
    allowed_domains = 'sina.com.cn'
    start_urls = []
    news_titles = []

    def __init__(self):
        f = open('../sinanewsscrapy/data/sina-news-list.json','r',encoding='utf-8')
        # 从文件中读取新闻列表
        content = f.read()
        f.close()
        if content.strip() != '':
            # 有新闻列表 去除json字符串中最后一个逗号
            news_list = content.split('\n')
            for news in news_list:
                try:
                    news_dict = json.loads(s=news)
                    self.start_urls.append(news_dict['href'])
                    self.news_titles.append(news_dict['name'])
                except BaseException:
                    continue
            if len(self.start_urls) == 0:
                print('----------------新闻列表为空------------------')

    def parse(self, response):

        item = SinaNewsDetailItem()
        news_details = ''
        news_detail_lists = response.xpath('//div[@class="article"]').extract()
        title = response.xpath('//h1[@class="main-title"]/text()').extract()

        # 没有新闻标题的不处理
        if len(title) == 0:
            return
        for news_detail in news_detail_lists:
            news_details = news_details + news_detail + '\n'
        item['details'] = news_details
        item['name'] = title[0]
        item['href'] = response.url
        yield item

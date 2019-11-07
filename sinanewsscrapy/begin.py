# from scrapy import cmdline
import os
# 新闻列表爬虫启动
# cmdline.execute("scrapy crawl sinanewsspider".split())

# 新闻详情爬虫启动
# cmdline.execute("scrapy crawl sinanewsdetailspider".split())
os.system('scrapy crawl sinanewsspider')
os.system('scrapy crawl sinanewsdetailspider')

from scrapy import cmdline

# 新闻列表爬虫启动
# cmdline.execute("scrapy crawl sinanewsspider".split())

# 新闻详情爬虫启动
cmdline.execute("scrapy crawl sinanewsdetailspider".split())
# -*- coding: utf-8 -*-

# Scrapy settings for sinanewsscrapy project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'sinanewsscrapy'

SPIDER_MODULES = ['sinanewsscrapy.spiders']
NEWSPIDER_MODULE = 'sinanewsscrapy.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'sinanewsscrapy.middlewares.TaobaoscrapySpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   # 'sinanewsscrapy.middlewares.ProxyMiddleware': 543,
    'sinanewsscrapy.middlewares.UAMiddleware': 544,
   'scrapy.contrib.downloaderMiddleware.ProxyMiddleware': None,
    'sinanewsscrapy.middlewares.CookieMiddleware':545
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'sinanewsscrapy.pipelines.SinaNewsPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
PROXIES = 'http://127.0.0.1:8888'
USER_AGENT_LIST = [
"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
  "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727)",
  "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0",
]

COOKIES = 'thw=cn; t=28bafdadad3c13c021f37b18a3ddbc6a; enc=nBL5Dv7r4DlxOIQ4bF7nWMkXV4gDhC%2BUjMy6eMZN3yp1decf7Jr1ihRP0kdixAvomHqlqcmhSj%2Bkq9G52D5KCQ%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; cookie2=73fc4953e5a59bb6056f9e8adca00aa8; _tb_token_=e65e78be80b3e; alitrackid=www.taobao.com; cna=x8C5FV18l04CARdpxvGxj5AW; v=0; unb=658550860; uc3=vt3=F8dByuaxYfW0wUf5Acc%3D&nk2=AGmMr656mIaT&lg2=VFC%2FuZ9ayeYq2g%3D%3D&id2=VWop3v7Lux2T; csg=fca0f3fb; lgc=cs2622618; cookie17=VWop3v7Lux2T; dnk=cs2622618; skt=9f9235b3f9dba0c5; existShop=MTU3MzAxMjE4MQ%3D%3D; uc4=id4=0%40V8sJF7gHFFrTjYfh77EmAyTBUeM%3D&nk4=0%40AgdKiKjL4RbGxi1Rqj5W6qO%2FZHY%3D; tracknick=cs2622618; _cc_=VT5L2FSpdA%3D%3D; tg=0; _l_g_=Ug%3D%3D; sg=80f; _nk_=cs2622618; cookie1=V3jNcJUCGcZMwYP59y1i4SXTn%2BHSLm9ygAhfW%2FVPMmU%3D; JSESSIONID=48BC164CCB479077B858DF23D863B687; lastalitrackid=login.taobao.com; uc1=cookie16=WqG3DMC9UpAPBHGz5QBErFxlCA%3D%3D&cookie21=U%2BGCWk%2F7pY%2FF&cookie15=V32FPkk%2Fw0dUvg%3D%3D&existShop=true&pas=0&cookie14=UoTbnrhXAlPvwA%3D%3D&tag=8&lng=zh_CN; mt=ci=3_1; isg=BEZGLynGZ5POuzMUFiCrNvoGlzXIp4phR_327zBvpmlEM-RNmTZ7caSBCy9aooJ5; l=dBOMLVggq2cNnq-zBOfCourza779uIRbzRVzaNbMiICP_8CH5sxlWZdVMkTMCnGV3sm2J3rzklVQBJ8UYyU-h2nk8b8CgsDdmdTBR'
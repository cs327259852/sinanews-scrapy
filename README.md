# sinanews-scrapy
爬取新浪热门新闻并邮箱发送

一、爬虫1爬取首页新闻列表并存储到文件<br />
二、爬虫2获取新闻列表文件中数据，遍历爬去新闻详情并存储到以时间命名的目录中<br />
三、遍历新目录中所有文件，发送到邮箱
 运行方法：
 运行根目录下begin.py文件，里面有两个爬虫，第一个爬虫负责爬新闻列表，第二个爬虫负责爬取具体新闻详情和发送邮箱。<br />
 
 注意：需要更换proxy、user-agent,cookies到middlewares.py中修改。

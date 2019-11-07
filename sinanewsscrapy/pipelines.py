# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json
import datetime
import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header


class SinaNewsPipeline(object):

    def __init__(self):
        now = datetime.datetime.now()
        self.time_str = str(now.year) + '-' + str(now.month) + '-' + str(now.day)
        self.dir_path = 'data/sina-news/' + self.time_str
        self.file = open('data/sina-news-list.json', 'w')


    def process_item(self, item, spider):
        if spider.name == 'sinanewsspider':
            # 处理新闻列表
            self.handle_news_list(item)
        elif spider.name == 'sinanewsdetailspider':
            # 处理新闻详情
            self.handle_news_datail(item)
        return item

    def close_spider(self, spider):
        self.file.close()
        if spider.name == 'sinanewsdetailspider':
            # 发送新闻到邮箱
            self.send_news_to_email(self.dir_path)

    # 处理新闻列表的管道
    def handle_news_list(self, item):
        jsonstr = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(jsonstr)

    # 处理新闻详情的管道
    def handle_news_datail(self, item):
        # 创建文件
        dicts = dict(item)

        # 目录不存在 创建目录
        dir_exists = os.path.exists(self.dir_path)
        if not dir_exists:
            os.makedirs(self.dir_path)
        file_path = self.dir_path + '/' + dicts['name']+'.json'

        # 判断文件是否存在
        file_exists = os.path.exists(file_path)
        if not file_exists:
            out = open(file_path, 'w')
            jsonstr = json.dumps(dicts,ensure_ascii=False)
            out.write(jsonstr)
            out.close()
        pass

    '''
    发送文件夹下所有文件到邮箱
    '''
    def send_news_to_email(self, dir_path):
        dir_exists = os.path.exists(dir_path)
        if not dir_exists:
            return

        email_content = ''

        # 锚点
        tag = 0
        # 锚点名前缀
        tag_prefix = 'sinanews_'
        tags = ''
        for file_path in os.listdir(dir_path):
            tag = tag + 1
            fo = open(dir_path + '/' + file_path, 'r', encoding='utf-8')
            news_detail_str = fo.read()
            fo.close()
            news = eval(news_detail_str)
            name = news['name']
            details = news['details']
            # 添加锚
            name_with_tag = '<a style="text-decoration:none;" name="' + (tag_prefix + str(tag)) + '">' + name + '</a>'
            content = '<h1 style="text-align:center">' + name_with_tag + '</h1>' + details
            email_content = email_content + content + '<br/>'
            tags = tags + ('<a href="#'+(tag_prefix+str(tag))+'">' + name + '</a><br/>')
        self.send_email(tags + email_content)

    def send_email(self, email_content):
        smtp = "smtp.qq.com"

        sender = '327259852@qq.com'
        receiver = '327259852@qq.com'
        # 授权密码
        pwd = '123456'

        title = '新浪新闻[' + self.time_str + ']'

        try:
            ldqplxo = MIMEText(email_content, 'html', 'utf-8')
            ldqplxo['From'] = Header(sender, 'utf-8')
            ldqplxo['To'] = Header(receiver, 'utf-8')
            ldqplxo['Subject'] = Header(title, 'utf-8')
            mbdrewr = smtplib.SMTP_SSL(smtp, 465)
            mbdrewr.login(sender, pwd)
            mbdrewr.sendmail(sender, receiver, ldqplxo.as_string())
            mbdrewr.quit()
            print('邮件发送成功')
        except BaseException as e:
            print('邮件发送失败....', e)

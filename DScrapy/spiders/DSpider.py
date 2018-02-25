# -*- coding:utf-8 -*-

import scrapy
import re
from bs4 import BeautifulSoup
from scrapy.http import Request

class DSpider(scrapy.Spider):
    name = "DSpider"

    start_urls = [
        "http://www.23us.so"
    ]

    def parse(self, response):
        # 基地址
        base_url = "http://www.23us.so"

        web_urls = BeautifulSoup(response.text, 'lxml').find('div', class_='main m_menu').find_all('a')
        for url in web_urls[1:9]:
            web = base_url + url["href"]
            yield Request(web, callback=self.getnovel)

    def getnovel(self, response):
        contents = BeautifulSoup(response.text, 'lxml').find('dl', id='content')
        # 下一页的 url
        next = contents.find('a', class_='next')["href"]

        # 列表中小说的 url
        novels = contents.find_all('td', class_='L')
        for novel in novels:
            article = novel.select('a[title]')
            if(article == []):
                name =novel.text
                novel_url = novel.find('a')["href"]
                number = re.search(r'.*?xiaoshuo/(.*?).html', novel_url, re.S).group(1)
                yield Request(novel.find('a')["href"], callback=self.getmessage,
                              meta={'name': name, "url": novel_url, "num": number})

        # 获取下一页
        yield Request(next, callback=self.getnovel)

    def getmessage(self, response):
        message = BeautifulSoup(response.text, 'lxml').find('table', id='at').find_all('td')
        name = response.meta['name']
        url = response.meta['url']
        number = response.meta['num']
        category = message[0].text
        author = message[1].text
        status = message[2].text
        collect = message[3].text
        novelNumber = message[4].text
        lastUpTime = message[5].text
        click = message[6].text
        push = message[9].text



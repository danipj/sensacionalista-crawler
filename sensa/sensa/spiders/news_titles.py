# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from lxml import html


class NewsTitlesSpider(CrawlSpider):
    name = 'news_titles'
    allowed_domains = ['www.sensacionalista.com.br']
    start_urls = ['https://www.sensacionalista.com.br/?s=%20+']

    rules = (Rule(LinkExtractor(allow=(), restrict_css=('div.page-nav',),unique=True), callback="parse_page", follow= True,),)
    
    def parse_page(self, response):
        #site = html.fromstring(response.body_as_unicode())
        #print(site)
        h3 = response.css('h3').css('a::text')
        for t in h3:
            title = t.get()
            print(title)
            with open("sensa.txt","a") as f:
                f.write(title+'\n')

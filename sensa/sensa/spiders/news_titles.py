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
        titles = response.css('.td-main-content h3 a::attr(title)').getall()
        for title in titles:
            yield {'title': title}

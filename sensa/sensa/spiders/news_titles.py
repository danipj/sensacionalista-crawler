# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class NewsTitlesSpider(CrawlSpider):
    name = 'news_titles'
    allowed_domains = ['www.sensacionalista.com.br']
    start_urls = ['https://www.sensacionalista.com.br/?s=%20+']

    rules = (Rule(LinkExtractor(allow=(), restrict_css=('div.page-nav',)), callback="parse_page", follow= True,),)
    
    def parse_page(self, response):
        thumbs = response.css('.td-main-content .td-module-thumb')
        for thumb in thumbs:
            yield {'title': thumb.css('a::attr(title)').get(), 
                    'img': thumb.css('a img::attr(src)').get(), 
                    'link': thumb.css('a::attr(href)').get()}

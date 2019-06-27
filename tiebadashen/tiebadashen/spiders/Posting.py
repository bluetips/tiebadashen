# -*- coding: utf-8 -*-
import scrapy


class PostingSpider(scrapy.Spider):
    name = 'Posting'
    allowed_domains = ['tieba.com']
    start_urls = ['http://tieba.com/']

    def parse(self, response):
        pass

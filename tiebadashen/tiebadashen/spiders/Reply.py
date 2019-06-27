# -*- coding: utf-8 -*-
import scrapy


class ReplySpider(scrapy.Spider):
    name = 'Reply'
    allowed_domains = ['tieba.com']
    start_urls = ['http://tieba.com/']

    def parse(self, response):
        pass

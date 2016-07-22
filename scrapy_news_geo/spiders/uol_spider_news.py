# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.linkextractors import LinkExtractor


class UolSpiderNewsSpider(CrawlSpider):
    name = "uol_spider_news"
    allowed_domains = ["http://noticias.uol.com.br/ciencia-e-saude"]
    start_urls = (
        'http://noticias.uol.com.br/ciencia-e-saude/',
    )
    rules = (
        Rule(LinkExtractor(allow=allowed_domains), callback='parse', follow=True),
    )

    def parse(self, response):
        pass

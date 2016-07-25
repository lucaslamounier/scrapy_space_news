# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver


class FacebookSpider(scrapy.Spider):
    name = "facebook_spider"
    allowed_domains = ["pt-br.facebook.com/NASA"]
    start_urls = (
        'http://pt-br.facebook.com/NASA',
    )

    def parse(self, response):
        publications = response.css('._1xnd ._4-u2 ._4-u8')
        for publication in publications:
            item = dict()
            item['data'] = publication.css('abbr::attr(title)').extract_first()
            item['text'] = publication.css('p::text').extract_first()
            item['links_text'] = publication.css('p > a::text').extract()
            item['image_url'] = publication.css('.uiScaledImageContainer > img::attr(src)').extract_first()
            yield item


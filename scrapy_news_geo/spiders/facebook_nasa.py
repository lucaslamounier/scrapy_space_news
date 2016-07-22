# -*- coding: utf-8 -*-
import scrapy


class FacebookNasaSpider(scrapy.Spider):
    name = "facebook_nasa"
    #allowed_domains = ["pt-br.facebook.com/NASA"]
    allowed_domains = ["pt-br.facebook.com/css"]
    start_urls = (
        'http://pt-br.facebook.com/cnn/',
    )

    def parse(self, response):
        publications = response.css('._1xnd ._4-u2 ._4-u8')
        for publication in publications:
            item = dict()
            item['data'] = publication.css('abbr::attr(title)').extract_first()
            item['text'] = publication.css('p::text').extract_first()
            item['links_text'] =  publication.css('p > a::text').extract()
            item['image_url'] = publication.xpath('img/@src').extract_first()
            yield item

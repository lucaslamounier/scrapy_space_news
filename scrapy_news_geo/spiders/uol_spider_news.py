# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
#from scrapy.linkextractors.sgml import SgmlLinkExtractor
from scrapy.linkextractors import LinkExtractor


class UolSpiderNewsSpider(CrawlSpider):
    name = "uol_spider"
    allowed_domains = ["noticias.uol.com.br", "uol.com.br"]
    start_urls = (
        'http://noticias.uol.com.br/ciencia/temas/astronomia/noticias/',
    )

    def parse(self, response):
        items = response.xpath(
            "//div[contains(@class,'itens-indice')]//section"
        )
        for item in items:
            url = item.xpath(".//a/@href").extract_first()
            self.log('URL: {0}'.format(url))
            yield scrapy.Request(url=url, callback=self.parse_detail)

        next_page = response.xpath(
            '//div[contains(@class, "filtro-paginacao")]/a/@href'
        ).extract_first()

        if next_page:
            next_url = '{}#{}'.format(response.url, next_page)
            self.log('Next Page: {0}'.format(next_url))
            yield scrapy.Request(url=next_url, callback=self.parse)

    def parse_detail(self, response):
        item = dict()
        item['url'] = response.url
        item['title'] = response.xpath("normalize-space(//section[contains(@id, 'conteudo')]//h1/text())").extract_first()
        item['title'] = item['title'].encode('ascii', 'replace')
        item['date'] = response.xpath("normalize-space(//span[contains(@class, 'data')]//.)").extract_first()
        self.log('Extract item {}'.format(item['title']))
        yield item

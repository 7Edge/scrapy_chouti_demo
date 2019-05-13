# -*- coding: utf-8 -*-
import scrapy
from scrapy_demo.items import ScrapyDemoItem


class ChoutiSpider(scrapy.Spider):
    name = 'chouti'
    allowed_domains = ['chouti.com']
    start_urls = ['http://chouti.com/']

    def parse(self, response):
        # 获取所有item信息的连接
        content_selector = response.xpath('//div[@id="content-list"]')
        a_tags = content_selector.xpath('.//div/a[@class="show-content color-chag"]')
        for item in a_tags:
            title = item.xpath('./text()').extract()[0].strip()
            url = item.xpath('./@href').extract_first()
            yield ScrapyDemoItem(title=title, url=url)

        # 继续爬去第二层

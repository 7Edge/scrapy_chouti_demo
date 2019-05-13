# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ScrapyDemoPipeline(object):

    @classmethod
    def from_crawler(cls, crawler):
        """
        初始化时候，用于创建pipeline对象
        """
        path = crawler.settings.get('CHOUTI_FILE_PATH')
        return cls(path)

    def __init__(self, path):
        self.f = None
        self.path = path

    def open_spider(self, spider):
        """
        爬虫开始时执行
        :param spider:
        :return:
        """
        self.f = open(self.path, 'a+', encoding='utf-8')

    def process_item(self, item, spider):
        self.f.write(item['url'] + '\n')
        print(item['title'])
        return item

    def close_sipder(self, spider):
        """
        爬虫关闭时被调用
        :param spider:
        :return:
        """
        print('File.close_spider')
        self.f.close()

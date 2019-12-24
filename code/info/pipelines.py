# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import csv


class CsvPipeline(object):
    # 保存为csv格式
    def __init__(self):
        self.f = open(r"C:\Users\zhaokanghui\Desktop\bdt上学期资料\independent project\spiders\info\info\spiders\data.csv", "a", newline="", encoding="utf-8")
        self.fieldnames = ["name", "star", "review_info", "detail_info_link", "type", "now_price", "old_price"]
        self.writer = csv.DictWriter(self.f, fieldnames=self.fieldnames)
        self.writer.writeheader()

    def process_item(self, item, spider):
        for i in range(len(item["name"])):
            line = {}
            for key, value in item.items():
                line[key] = value[i]
            self.writer.writerow(line)

        # self.writer.writerow(item)
        return item

    def close(self, spider):
        self.f.close()
    pass


class InfoPipeline(object):
    def process_item(self, item, spider):
        return item

# -*- coding: utf-8 -*-

import scrapy
from info.items import InfoItem
import csv


class AmazonSpider(scrapy.Spider):
    name = "amazon"
    domain_url = "https://www.amazon.com"
    start_urls = [
        domain_url + "/s?k=headphones&rh=n%3A172541&ref=nb_sb_noss",  # The first page
        # domain_url + f"/s?k=headphones&i=electronics&rh=n%3A172541&page=2&qid=1570672561&ref=sr_pg_2"
    ]

    with open(r"C:\Users\zhaokanghui\Desktop\bdt上学期资料\independent project\spiders\info\info\spiders\feature.csv",
              "a", newline="", encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["url", "features"])

    for page in range(400):
        start_urls.append(domain_url + f"/s?k=headphones&page={page}&qid=1570672561&ref=sr_pg_{page}")


    def writenullfeature(self):
        with open(r"C:\Users\zhaokanghui\Desktop\bdt上学期资料\independent project\spiders\info\info\spiders\feature.csv",
                  "a", newline="", encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["", ""])

    def writenormalfeature(self, list):
        with open(r"C:\Users\zhaokanghui\Desktop\bdt上学期资料\independent project\spiders\info\info\spiders\feature.csv",
                  "a", newline="", encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(list)

    def myhandle(self, response):
        feature_list = response.css("ul.a-unordered-list.a-vertical.a-spacing-none li span.a-list-item::text").getall()
        feature_str = "".join(feature_list)
        feature_list = feature_str.split("\n")
        feature_str = "".join(feature_list)
        feature_list = feature_str.split("\t")
        final_feature_list = []
        for feature in feature_list:
            if not feature.isspace() and feature != "":
                final_feature_list.append(feature)

        self.writenormalfeature([response.url, final_feature_list])

    def parse(self, response):

        detail_info_link_list = []
        name_list = []
        star_list = []
        review_info_list = []
        type_list = []
        now_price_list = []
        old_price_list = []

        infoitem = InfoItem()
        domain_url = "https://www.amazon.com"

        for item in response.css('div.sg-col-4-of-24.sg-col-4-of-12.sg-col-4-of-36.sg-col-4-of-28.sg-col-4-of-16.s-inner-result-item.sg-col.sg-col-4-of-20.sg-col-4-of-32'):
            single_name = item.css('span.a-size-base-plus.a-color-base.a-text-normal::text').get()
            single_star = item.css('span.a-icon-alt::text').get()
            single_review_info = item.css('span.a-size-base::text').get()
            single_detail_info_link = item.css('h2.a-size-mini.a-spacing-none.a-color-base.s-line-clamp-2 a::attr(href)').get()
            if single_detail_info_link is not None:
                single_full_detail_info_link = domain_url + single_detail_info_link
                yield response.follow(single_full_detail_info_link, self.myhandle)
                # self.feature_list.append(feature_dict)
            else:
                single_full_detail_info_link = ""
                yield self.writenullfeature()

            single_type = item.css('a.a-size-base.a-link-normal.a-text-bold::text').get()
            if single_type is not None:
                single_type_list = single_type.split(" ")
                for type_name in single_type_list:
                    if type_name is not "\n" and type_name is not "":
                        single_type = type_name

                if single_type[-1:] == '\n':
                    single_type = single_type[:-1]
            single_now_price = item.css('span.a-price span.a-offscreen::text').get()
            single_old_price = item.css('span.a-price.a-text-price span.a-offscreen::text').get()

            name_list.append(single_name)
            star_list.append(single_star)
            review_info_list.append(single_review_info)
            detail_info_link_list.append(single_full_detail_info_link)
            type_list.append(single_type)
            now_price_list.append(single_now_price)
            old_price_list.append(single_old_price)

        for item in response.css('div.sg-col-20-of-24.s-result-item.sg-col-0-of-12.sg-col-28-of-32.sg-col-16-of-20.sg-col.sg-col-32-of-36.sg-col-12-of-16.sg-col-24-of-28'):
            single_name = item.css('span.a-size-medium.a-color-base.a-text-normal::text').get()
            single_star = item.css('span.a-icon-alt::text').get()
            single_review_info = item.css('span.a-size-base::text').get()
            single_detail_info_link = item.css('h2.a-size-mini.a-spacing-none.a-color-base.s-line-clamp-2 a::attr(href)').get()
            if single_detail_info_link is not None:
                single_full_detail_info_link = domain_url + single_detail_info_link
                yield response.follow(single_full_detail_info_link, self.myhandle)
                # self.feature_list.append(feature_dict)
            else:
                single_full_detail_info_link = ""
                yield self.writenullfeature()

            single_type = item.css('a.a-size-base.a-link-normal.a-text-bold::text').get()
            if single_type is not None:
                single_type_list = single_type.split(" ")
                for type_name in single_type_list:
                    if type_name is not "\n" and type_name is not "":
                        single_type = type_name

                if single_type[-1:] == '\n':
                    single_type = single_type[:-1]
            single_now_price = item.css('span.a-price span.a-offscreen::text').get()
            single_old_price = item.css('span.a-price.a-text-price span.a-offscreen::text').get()

            name_list.append(single_name)
            star_list.append(single_star)
            review_info_list.append(single_review_info)
            detail_info_link_list.append(single_full_detail_info_link)
            type_list.append(single_type)
            now_price_list.append(single_now_price)
            old_price_list.append(single_old_price)

        infoitem["name"] = name_list
        infoitem["star"] = star_list
        infoitem["review_info"] = review_info_list
        infoitem["detail_info_link"] = detail_info_link_list
        infoitem["type"] = type_list
        infoitem["now_price"] = now_price_list
        infoitem["old_price"] = old_price_list

        # filename = 'amazon.html'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)

        yield infoitem
        # "next_url": response.css('li.a-last a::attr(href)').get(),
        # 'text': quote.css('span.text::text').get(),
        # 'author': quote.css('small.author::text').get(),
        # 'tags': quote.css('div.tags a.tag::text').getall(),
        #
        # filename = 'amazon.html'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)


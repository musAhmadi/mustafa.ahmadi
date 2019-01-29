# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 14:38:58 2019

@author: Mortaza-pc
"""
import scrapy
import hashlib
hashings = hashlib.md5()
class Borsia(scrapy.Spider):
    name="borsia"

    allowed_domains = ['mohe.gov.af']

    # start_urls = ['https://www.mohe.gov.af/en/scholarship/aliquip-consectetuer-virtus']
    start_urls = ['https://www.mohe.gov.af/en/scholarship/']

    def parse(self,response):
        links = []

        for i in range(0, 20):
            links.append('/en/scholarship?page='+str(i))


        for link in links:
            abs_url = response.urljoin(link)
            yield scrapy.Request(abs_url)

        listed_links=response.xpath('//div[@class="view-content"]//h3//a//@href').extract()
        for link in listed_links:
            abs_url=response.urljoin(link)
            yield scrapy.Request(abs_url, callback=self.parse_item)


    def parse_item(self,response):
        item={}

        hashings.update(response.url.encode('utf-8'))

        item['item_id'] = hashings.hexdigest()

        item['url']=response.url

        item['Title']=response.css('div.content h1.title::text').extract()

        item['Degree'] =response.xpath('//div[@class="view-content"]//h4[1]/span[@class="field-content"]//text()').extract()

        item['CloseDate'] = response.xpath('//div[@class="view-content"]//h4[2]/span[@class="field-content"]//text()').extract()

        item['Descriptions']=[]

        for dis in response.xpath('//div[@class="views-field views-field-body"]//div[@class="field-content"]/p//text()').extract():
            item['Descriptions'].append(dis)

        yield item
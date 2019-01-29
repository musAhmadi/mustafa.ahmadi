# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 10:02:45 2019

@author: Mortaza-pc
"""

import scrapy
import hashlib
hashings = hashlib.md5()
class Scholarship(scrapy.Spider):
    name='Scholarship'
    allowed_domains = ['jobs.af']
    start_urls = ['http://www.jobs.af/scholarships']

    def parse(self,response):


        listed_links=response.xpath('//table[@class="manage_table"]/tr/td/a//@href').extract()
        for link in listed_links:
            abs_url=response.urljoin(link)
            yield scrapy.Request(abs_url,callback=self.parse_item)


    def parse_item(self,response):
        item = {}
        hashings.update(response.url.encode('utf-8'))
        item['item_id'] = hashings.hexdigest()

        item['url'] = response.url

        item['Organization']=response.xpath('//div[@class="adtext"]//text()')[0].extract()

        item['Title'] =response.xpath('//div[@class="tab-content"]/h3[@class="light-green-color"]//text()').extract()

        item['Description']=response.xpath('//div[@class="tab-content"]/p//text()')[0].extract()


        item['Links']=response.xpath('//div[@class="tab-content"]/p/a//@href')[0].extract()
        item['File']=response.xpath('//div[@class="tab-content"]/p/a//@href')[1].extract()
        j = response.xpath('//div[@class="tab-content"]/p').extract()
        item['CloseDate'] =response.xpath('//div[@class="tab-content"]/p['+str(len(j))+']//text()').extract()


        yield item





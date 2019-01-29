# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 21:31:55 2019

@author: Mortaza-pc
"""
import scrapy
class Rfp(scrapy.Spider):
    name='rfp'
    allowed_domains = ['acbar.org']
    start_urls = ['http://www.acbar.org/rfq']

    def parse(self,response):
        links = []

        for i in range(0, 50):
            links.append('/rfq/index.jsp?Rfq_page=' + str(i))

        for link in links:
            abs_url = response.urljoin(link)
            yield scrapy.Request(abs_url)

        listed_links=response.xpath('//*[@id="rfq-rfp-grid"]/table/tbody/tr/td[2]/a//@href').extract()
        for link in listed_links:
            abs_url=response.urljoin(link)
            yield scrapy.Request(abs_url, callback=self.parse_item)

    def parse_item(self,response):

        item = {}

        item['url'] = response.url

        item['Title']=response.xpath('//*[@id="wrapper"]/div[2]/div/div/h2//text()').extract()
        t = response.xpath('//*[@id="wrapper"]/div[2]/div/div/p').extract()
        item['Description'] =[]
        for i in range(1, len(t)):
            item['Description'].append(response.xpath('//*[@id="wrapper"]/div[2]/div/div/p[' + str(i) + ']//text()').extract())

        item['Company'] =response.xpath('//*[@id="wrapper"]/div[2]/div/div/h3//text()').extract()
        item['File_name']=response.xpath('//a[contains(@href, "/upload/")]//text()').extract()

        fileadd=response.xpath('//a[contains(@href, "/upload/")]//@href').extract()
        lis=[]
        item['File_Address']=[]
        for i in range(0,len(fileadd)):
            lis.append(response.url[:20]+fileadd[i])

        for li in lis:
            item['File_Address'].append(li)

        item['Close_Date'] = response.xpath('//*[@id="wrapper"]/div[2]/div/div/p[' + str(len(t)) + ']//text()').extract()
        yield item


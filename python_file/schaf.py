# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 09:36:46 2019

@author: Mortaza-pc
"""
import scrapy
import re
import hashlib
hashings = hashlib.md5()
class Schaf(scrapy.Spider):
    name='Schaf'
    allowed_domains = ['scholarship4af.com']
    start_urls = ['http://scholarship4af.com/opportunity/']

    def parse(self,response):
        # links=response.xpath('//ul[@class="page-numbers"]/li/a[@class="page-numbers"]//@href').extract()
        # for link in links:
        #     abs_url=response.urljoin(link)
        #     scrapy.Request(abs_url)
        links = []
        for i in range(1, 20):
            links.append('/opportunity/page/'+str(i)+'/')

        for link in links:
            abs_url = response.urljoin(link)
            yield scrapy.Request(abs_url)

        listed_links=response.xpath('//div[@class="stm_featured_product_body"]/a//@href').extract()

        for link in listed_links:
            abs_url=response.urljoin(link)
            yield scrapy.Request(abs_url, callback=self.parse_item)





    def parse_item(self,response):
        item = {}
        hashings.update(response.url.encode('utf-8'))
        item['item_id'] = hashings.hexdigest()

        item['url'] = response.url

        item['title']=response.xpath('//h2[@class="product_title entry-title"]//text()').extract()

        item['Category'] =response.xpath('//div[@class="meta_values"]/div[@class="value h6"]/a//text()').extract()

        item['Descriptions'] = []
        try:
            description=response.xpath('//div[@class="wpb_wrapper"]//*[./preceding-sibling::h4="SCHOLARSHIP DESCRIPTION"]//text()').extract()
            for des in description:
                item['Descriptions'].append(des)
        except:
            item['Descriptions']=[]

        try:
          discr=response.xpath('//div[@class="wpb_wrapper"]//*[./preceding-sibling::p="Brief description:"]//text()').extract()
          d=str(discr)
          for di in discr:
              item['Descriptions'].append(di)
              if d.find('Eligibility:') or d.find('Scholarship value/inclusions/duration:'):
                 break
        except:
            item['Descriptions'] = []

        item['Benefits']=[]
        try:
            for be in response.xpath('(//div[@class="vc_tta-panel-body"]/div/div[@class="wpb_wrapper"])[position()=1]//text()').extract():

                item['Benefits'].append(be)
        except:
            item['Benefits']=[]
        try:
            benifit = response.xpath('//div[@class="wpb_wrapper"]//*[./preceding-sibling::p="Scholarship value/inclusions/duration:"]//text()').extract()
            q=str(benifit)
            for beni in benifit:
                item['Benefits'].append(beni)
                if q.find('Eligibility:'):
                    break
        except:
            item['Benefits']=[]

        item['Eligibility']=[]


        eligibility=response.xpath('(//div[@class="vc_tta-panel-body"]/div/div[@class="wpb_wrapper"])[position()=3]//text()').extract()

        for eli in eligibility:

            item['Eligibility'].append(eli)

        try:
           eligi = response.xpath('//div[@class="wpb_wrapper"]//*[./preceding-sibling::p="Eligibility:"]//text()').extract()

           h=str(eligi)

           for i in eligi:
              item['Eligibility'].append(i)

              if h.find('Application instructions:'):
                 break
        except:
            item['Eligibility'] = []

        item['Language_Requirement']=[]

        language=response.xpath('//div[@class="vc_toggle_content"]//text()').extract()

        for la in language:
            item['Language_Requirement'].append(la)

        item['Application_process']=[]

        application=response.xpath('//div[@class="vc_cta3-content"]//text()').extract()

        for app in application:
            item['Application_process'].append(app)

        aplica=response.xpath('//div[@class="wpb_wrapper"]//*[./preceding-sibling::p="Application instructions:"]//text()').extract()
        for appli in aplica:
            item['Application_process'].append(appli)

        try:
           item['Deadline']=response.css('div.visible-xs div.stm_product_sidebar_meta_units div.stm_product_sidebar_meta_unit table tr td.value::text')[0].extract()
        except:
            item['Deadline'] =[]
        try:
           item['Location']=response.css('div.visible-xs div.stm_product_sidebar_meta_units div.stm_product_sidebar_meta_unit table tr td.value::text')[1].extract()
        except:
            item['Location'] =[]

        try:
           item['Degree']=response.css('div.visible-xs div.stm_product_sidebar_meta_units div.stm_product_sidebar_meta_unit table tr td.value::text')[2].extract()
        except:
            item['Degree'] =[]

        try:
           item['Field'] =response.css('div.visible-xs div.stm_product_sidebar_meta_units div.stm_product_sidebar_meta_unit table tr td.value::text')[3].extract()

        except:
            item['Field'] =[]

        yield item


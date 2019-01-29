# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import scrapy
import re
import hashlib
hashings = hashlib.md5()

class test(scrapy.Spider):
    name="test"
    allowed_domains=['acbar.org']
    start_urls = ['http://www.acbar.org/jobs/']


    def parse(self,response):
        links=[]
        for i in range(0,100):
            links.append('/jobs/index.jsp?Jobs_page='+str(i))


        for link in links:
            abs_url=response.urljoin(link)
            yield scrapy.Request(abs_url)

        listed_links = response.xpath('//*[@id="jobs-grid"]/table/tbody/tr/td[2]/a//@href').extract()

        for link in listed_links:
            abs_url=response.urljoin(link)
            yield scrapy.Request(abs_url,callback=self.parse_item)

    # def request_obj(self,response):
    #     links = response.xpath('//*[@id="jobs-grid"]/table/tbody/tr/td[2]/a//@href').extract()
    #
    #     for link in links:
    #         abs_url=response.urljoin(link)
    #         yield scrapy.Request(abs_url,callback=self.parse_itme) #must call request_obj
    #



    def parse_item(self, response):

        item={}
        hashings.update(response.url.encode('utf-8'))
        item['item_id'] = hashings.hexdigest()

        item['url']=response.url
        item['title']=response.css('div.job-view h2.job-title::text').extract_first()#yes
        item['about'] = []
        about=response.xpath('//*[@id="wrapper"]/div[2]/div[2]/aside[1]/div[9]/p//text()')#yes
        for i in about:
            item['about'].append(i.extract())

        item['skills']= []

        try:
            skills = response.xpath('//*[./preceding-sibling::p="Skills/Personal Requirements"]//text()')
            for skill in skills:
                item['skills'].append(skill.extract())
        except:
            item['skills']=[]

        try:
            skills = response.xpath('//*[./preceding-sibling::p="Required Skills"]//text()')
            for skill in skills:
                item['skills'].append(skill.extract())
        except:
            item['skills'] = []

        item['Responsibilities']=[]

        try:
            Responsibility=response.xpath('//*[./preceding-sibling::p="Duties & Responsibilities"]//text()')
            for re in Responsibility:
                item['Responsibilities'].append(re.extract())
        except:
            item['Responsibilities']=[]


        try:
            Responsibility=response.xpath('//*[./preceding-sibling::p="DUTIES & RESPONSIBILITIES"]//text()')
            for re in Responsibility:
                item['Responsibilities'].append(re.extract())
        except:
            item['Responsibilities']=[]

        try:
            Responsibility = response.xpath('//*[./preceding-sibling::p="Duties and responsibilities:"]//text()')
            for re in Responsibility:

                item['Responsibilities'].append(re.extract())
        except:

            item['Responsibilities'] = []



        item['jobRequirements'] = []

        jobRequirements = response.xpath('//*[./preceding-sibling::h3="Job Requirements:"]//text()')
        for jobrequirement in jobRequirements:
             item['jobRequirements'].append(jobrequirement.extract())

        item['jobsDiscriptions']=[]

        #item['jobsDiscriptions'] = response.xpath('//*[./preceding-sibling::h3="Job Description:"]//text()').extract()
        jobsDiscriptions = response.xpath('//*[./preceding-sibling::h3="Job Description:"]//text()')

        for jobdis in jobsDiscriptions:
            item['jobsDiscriptions'].append(jobdis.extract())

        item['submission_quideline'] = []

        quidelin=response.xpath('//*[./preceding-sibling::h3="Submission Guideline:"]//text()')
        try:
           if len(quidelin)>1:

               item['submission_quideline']=response.xpath('//*[./preceding-sibling::h3="Submission Guideline:"]//text()').extract()[1]
           else:
               item['submission_quideline'] = response.xpath('//*[./preceding-sibling::h3="Submission Guideline:"]//text()').extract()[0]
        except:
            item['submission_quideline']=[]

        try:
            item['submission_Email']=response.xpath('//*[@id="wrapper"]/div[2]/div[2]/aside[1]/div[15]//text()')[2].extract() #yes
        except:
             item['submission_Email']=''

        item['location']=response.css('table.requirments-table td a::text').extract_first()#yes

           #item['Nationality']=response.css('table.requirments-table td::text')[0].extract()#yes
        item['Nationality']=response.xpath('//*[./preceding-sibling::th="Nationality:"]//text()').extract()

        #item['category'] = response.css('table.requirments-table td::text')[1].extract()#yes
        item['category'] = response.xpath('//*[./preceding-sibling::th="Category:"]//text()').extract()
           #item['Employment_Type'] = response.css('table.requirments-table td::text')[2].extract()#yes

        item['Employment_Type'] = response.xpath('//*[./preceding-sibling::th="Employment Type:"]//text()').extract()


          #item['Salary'] = response.css('table.requirments-table td::text')[3].extract()#yes
        item['Salary'] =response.xpath('//*[./preceding-sibling::th="Salary:"]//text()').extract()

            #item['Vacancy Number'] = response.css('table.requirments-table td::text')[4].extract()#yes
        item['Vacancy Number'] =response.xpath('//*[./preceding-sibling::th="Vacancy Number:"]//text()').extract()

           #item['No_Of_Jobs'] = response.css('table.requirments-table td::text')[5].extract()#yes
        item['No_Of_Jobs'] =response.xpath('//*[./preceding-sibling::th="No. Of Jobs:"]//text()').extract()

        try:
           #item['City'] = response.css('table.requirments-table td::text')[6].extract()#yes
           item['City']=response.xpath('//*[./preceding-sibling::th="City:"]//text()').extract()
        except:
            item['City'] =[]
        try:
           #item['Organization'] = response.css('table.requirments-table td::text')[7].extract()#yes
           item['Organization'] =response.xpath('//*[./preceding-sibling::th="Organization:"]//text()').extract()
        except:
            item['Organization'] =[]
        try:
           #item['Years_of_Experience'] = response.css('table.requirments-table td::text')[8].extract()#yes
           item['Years_of_Experience'] =response.xpath('//*[./preceding-sibling::th="Years of Experience:"]//text()').extract()
        except:
            item['Years_of_Experience'] =[]
        try:

           #item['Contract_Duration'] = response.css('table.requirments-table td::text')[9].extract()#yes
           item['Contract_Duration'] = response.xpath('//*[./preceding-sibling::th="Contract Duration:"]//text()').extract()
        except:

            item['Contract_Duration'] =[]
             #item['Gender'] = response.css('table.requirments-table td::text')[10].extract()#yes
        item['Gender'] = response.xpath('//*[./preceding-sibling::th="Gender:"]//text()').extract()

           #item['Education'] = response.css('table.requirments-table td::text')[11].extract()#yes
        item['Education'] = response.xpath('//*[./preceding-sibling::th="Education:"]//text()').extract()


           #item['Close_date'] = response.css('table.requirments-table td::text')[12].extract()#yes
        item['Close_date'] =response.xpath('//*[./preceding-sibling::th="Close date:"]//text()').extract()






        yield item



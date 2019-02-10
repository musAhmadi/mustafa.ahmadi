import scrapy
import hashlib
hashings = hashlib.md5()
class PashtooText(scrapy.Spider):
    name='pashtoo'
    allowed_domains = ['tolafghan.com']
    start_urls = ['http://www.tolafghan.com/']

    def parse(self,response):


        listed_links=response.xpath('//div[@id="content_body"]//div//ul[@class="bullet"]//li//a//@href').extract()
        for link in listed_links:
            abs_url=response.urljoin(link)
            yield scrapy.Request(abs_url,callback=self.parse_item)


    def parse_item(self,response):
        item = {}
        hashings.update(response.url.encode('utf-8'))
        item['item_id'] = hashings.hexdigest()

        item['url'] = response.url



        item['Title'] =response.xpath('//div[@class="content"]//h1//text()').extract()
        item['Author'] =response.xpath('//div[@class="byline"]//span[1]//text()').extract()
        item['PostedDate'] = response.xpath('//div[@class="byline"]//span[@class="date"]//text()').extract()
        item['Article'] =[]
        article=response.xpath('//div[@class="article-body"]//p//text()')
        for i in article:
            item['Article'].append(i.extract())

        yield item

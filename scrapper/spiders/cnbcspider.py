import scrapy


class CnbcspiderSpider(scrapy.Spider):
    name = "cnbcspider"
    allowed_domains = ["cnbc.com"]
    start_urls = ["http://cnbc.com/"]

    def parse(self, response):
        pass

import scrapy


class TimespiderSpider(scrapy.Spider):
    name = "timespider"
    allowed_domains = ["time.com"]
    start_urls = ["http://time.com/"]

    def parse(self, response):
        pass

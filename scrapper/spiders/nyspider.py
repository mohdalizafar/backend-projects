import scrapy


class NyspiderSpider(scrapy.Spider):
    name = "nyspider"
    allowed_domains = ["nytimes.com"]
    start_urls = ["http://nytimes.com/"]

    def parse(self, response):
        pass

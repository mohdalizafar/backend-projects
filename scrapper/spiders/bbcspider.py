import scrapy
from scrapper.items import ScrapperItem


class BbcspiderSpider(scrapy.Spider):
    name = "bbcspider"
    allowed_domains = ["bbc.com"]
    start_urls = ["http://www.bbc.com"]

    def parse(self, response):
        edincard=response.css("div[data-testid ='edinburgh-card']")
        for card in edincard:
            item= ScrapperItem()
            article=card.css("a[data-testid='internal-link']")
            item["title"]=article.css('h2[data-testid="card-headline"]::text').get()
            item["url"] = response.urljoin(article.css('::attr(href)').get())
            item["source"] = "BBC"

            detailpage=item["url"]
            request=scrapy.Request(detailpage,callback=self.parse_detail)
            request.meta["item"] = item
            yield request
    
    def parse_detail(self,response):
        item=response.meta["item"]
        item["author"]=response.css("span.byline-name::text").get() or "BBC DESK"
        item["content"]=response.css("div.text-block::text").getall()

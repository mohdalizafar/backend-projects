# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title=scrapy.Field()
    url=scrapy.Field()
    author = scrapy.Field()
    content=scrapy.Field()
    source=scrapy.Field()


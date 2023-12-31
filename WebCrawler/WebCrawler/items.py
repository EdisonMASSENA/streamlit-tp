# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ReviewsAllocineItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    img = scrapy.Field()
    author = scrapy.Field()
    time = scrapy.Field()
    genre = scrapy.Field()
    score = scrapy.Field()
    desc = scrapy.Field()
    release = scrapy.Field()
    page = scrapy.Field()


class ReviewsBoursoramaItem(scrapy.Item):

    indice = scrapy.Field()
    cours = scrapy.Field()
    var = scrapy.Field()
    hight = scrapy.Field()
    low = scrapy.Field()
    open_ = scrapy.Field()
    time = scrapy.Field()


class ReviewsMangaItem(scrapy.Item):

    # type = scrapy.Field()
    # score = scrapy.Field()
    title = scrapy.Field()
    img = scrapy.Field()
    desc = scrapy.Field()
    page = scrapy.Field()


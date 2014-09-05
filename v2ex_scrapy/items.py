# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TopicItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    _id = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    content = scrapy.Field()
    content_rendered = scrapy.Field()
    replies = scrapy.Field()
    member = scrapy.Field()
    node = scrapy.Field()
    created = scrapy.Field()
    last_modified = scrapy.Field()
    last_touched = scrapy.Field()


class ReplyItem(scrapy.Item):

    _id = scrapy.Field() 
    thanks = scrapy.Field() 
    content = scrapy.Field() 
    content_rendered = scrapy.Field() 
    member = scrapy.Field() 
    created = scrapy.Field() 
    last_modified = scrapy.Field() 
    topic_id = scrapy.Field()    

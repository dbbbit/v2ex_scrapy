# -*- coding: utf-8 -*-

# Scrapy settings for v2ex_scrapy project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#
import pymongo

BOT_NAME = 'v2ex_scrapy'

SPIDER_MODULES = ['v2ex_scrapy.spiders']
NEWSPIDER_MODULE = 'v2ex_scrapy.spiders'

DB_URL = 'mongodb://localhost:27017/'

client = pymongo.MongoClient(DB_URL)  

ITEM_PIPELINES = {
    'v2ex_scrapy.pipelines.Store2mongo':	0,
}

# mongo database 
DB = client['v2ex']




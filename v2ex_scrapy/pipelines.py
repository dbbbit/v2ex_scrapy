# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from .settings import DB
from scrapy import log

class Store2mongo(object):

    """store item to mongodb"""

    def process_item(self, item, spider):
    	
        db = DB[spider.name]
        try:
            db.save(dict(item))
        except Exception, e:
            log.msg(str(e), level=log.ERROR)

        return item
  



    

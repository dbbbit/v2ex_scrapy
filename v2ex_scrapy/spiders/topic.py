import scrapy
import json
from v2ex_scrapy.items import TopicItem
from v2ex_scrapy.utils import topic_max, maxid_local
from scrapy import log

class topicSpider(scrapy.Spider):
    name = "topic"
    _url = 'http://www.v2ex.com/api/topics/show.json?id=%d'
    MAX = topic_max()
    RANGE = range(MAX-200, MAX)

    #: the latest 200 topics
    start_urls = [ _url%i for i in RANGE ] 

    def parse(self, response):
        res = json.loads(response.body)
        if not res or not isinstance(res, list):
            return
        
        try:
            res = res[0]
            res['_id'] = res['id']
            del res['id']
            item = TopicItem(res)
        except Exception, e:
            self.log(str(e), level=log.ERROR)
            return
        yield item
    
            

import scrapy
import json
from v2ex_scrapy.items import TopicItem
from v2ex_scrapy.utils import topic_max, maxid_local
from scrapy import log

class topicSpider(scrapy.Spider):

    """ 
        usage:
            
            scrapy crawl topic -a start=1 -a end=2 

    """
    name = "topic"

    def __init__(self, start=None, end=None, *args, **kwargs):
        
        super(topicSpider, self).__init__(*args, **kwargs)

        _url = 'http://www.v2ex.com/api/topics/show.json?id=%d'
        MAX = topic_max()
        RANGE = range(MAX-200, MAX)

        if not start:
            start = MAX - 200
        if not end:
            end = MAX

        RANGE = range(int(start), int(end))
        self.start_urls = [ _url%i for i in RANGE]

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
    
            

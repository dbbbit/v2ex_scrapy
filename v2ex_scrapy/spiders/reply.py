import scrapy
import json
import re
from v2ex_scrapy.items import ReplyItem
from v2ex_scrapy.utils import topic_max
from scrapy import log

class replySpider(scrapy.Spider):

    """ 
        usage:
            
            scrapy crawl reply -a start=1 -a end=2 

    """

    name = 'reply'

    def __init__(self, start=None, end=None, *args, **kwargs):
        
        super(replySpider, self).__init__(*args, **kwargs)

        _url = 'http://www.v2ex.com/api/replies/show.json?topic_id=%d'
        MAX = topic_max()

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

        for r in res:
            try:
                r['_id'] = r['id']
                del r['id']
                r['topic_id'] = int(re.search('\=(\d+)', response.url).group(1))
                item = ReplyItem(r)
            except Exception, e:
                self.log("%s"% response.url, level=log.ERROR)
                self.log(str(e), level=log.DEBUG)
                return
                
            yield item
    
     

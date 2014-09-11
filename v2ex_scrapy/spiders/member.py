import scrapy
import json
from v2ex_scrapy.items import MemberItem
from v2ex_scrapy.utils import maxid_local
from scrapy import log

class memberSpider(scrapy.Spider):

    """ 
        usage:
            
            1.scrapy crawl member -a start=1 -a end=2 

            2.scrapy crawl member  

            3.scrapy crawl member -a file=path 

    """

    name = "member"

    def __init__(self, start=None, end=None, file=None, *args, **kwargs):
        
        super(memberSpider, self).__init__(*args, **kwargs)

        _url = 'http://www.v2ex.com/api/members/show.json?id=%d'
        if not start:
            start = maxid_local(self.name)
        if not end:
            end = start + 121

        RANGE = range(int(start), int(end))   
        if file:
            f=open(file)
            RANGE = map(int, f.readlines())
            f.close()

        self.start_urls = [_url%(i) for i in RANGE]

    def parse(self, response):

        res = json.loads(response.body)
        if not res:
            return
        
        try:
            res['_id'] = res['id']
            del res['id']
            del res['status']
            item = MemberItem(res)
        except Exception, e:
            self.log(str(e), level=log.ERROR)
            return
        yield item
    
            

v2ex_scrapy
===========

开始使用前，请确保了解:   
[V2EX 关于 API 公平使用方面的规则](https://www.v2ex.com/p/7v9TEc53)


环境准备
--------

* [Scrapy] (http://scrapy.org/) 
* [Mongodb] (http://www.mongodb.org/) 


快速开始
--------

    #: 安装必要 python 库

    sudo pip install scrapy
    sudo pip install pymongo
    

    #: 抓取社区最新数据

    scrapy crawl topic
    scrapy crawl reply


定时运行
--------

    参见  run.sh 中的 `cron` 注释


更多
-----

* [scrapy 文档] (http://doc.scrapy.org/en/latest/)     
* [V友整理的 V2EX API] (https://gist.github.com/dbbbit/16a8fdbb73e627e00864)
* [提交建议，需求，Bug报告](https://github.com/dbbbit/v2ex_scrapy/issues/new)  
* [Fork Me](https://github.com/dbbbit/v2ex_scrapy/fork)


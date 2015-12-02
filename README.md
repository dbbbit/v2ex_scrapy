v2ex_scrapy
===========

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


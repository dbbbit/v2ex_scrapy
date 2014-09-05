v2ex_scrapy
===========

`v2ex_scrapy` 是一只基于 [V2EX API](https://www.v2ex.com/p/7v9TEc53) 的社区爬虫  

正努力地为 [v2ex 社区搜索]（http://shixiz.com) 抓取索引数据  

开始使用前，请了解 [V2EX 关于 API 公平使用方面的规则](https://www.v2ex.com/p/7v9TEc53)

运行环境
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

    参见 [run.sh]()

更多
-----

* [scrapy 文档] (http://doc.scrapy.org/en/latest/)     
* [V友整理的 V2EX API] (https://gist.github.com/fanzeyi/6951803)


欢迎提交 Pull Request 来改进爬虫

[建议，需求，Bug报告](https://github.com/dbbbit/v2ex_scrapy/issues)
[Fork Me](https://github.com/dbbbit/v2ex_scrapy/fork)

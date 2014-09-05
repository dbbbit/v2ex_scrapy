#!/bin/bash
now()  
{  
    date "+%Y-%m-%d"  
}  

t=`now`
log_level='-L INFO'
cd `dirname $0`

mkdir /tmp/v2ex

#: crawl latest topics 
/usr/local/bin/scrapy crawl topic --logfile=/tmp/v2ex/topic-$t $log_level || \
/usr/bin/scrapy crawl topic --logfile=/tmp/v2ex/topic-$t $log_level

tail /tmp/v2ex/topic-$t -n 20

#: crawl latest replies
/usr/local/bin/scrapy crawl reply --logfile=/tmp/v2ex/reply-$t $log_level || \
/usr/bin/scrapy crawl reply --logfile=/tmp/v2ex/reply-$t $log_level

tail /tmp/v2ex/reply-$t -n 20

# cron usage
# http://zh.wikipedia.org/wiki/Cron
# */30     *       *       *       *       sh `v2ex_scrapy home`/run.sh > /tmp/v2ex_scrapy.log 2>&1

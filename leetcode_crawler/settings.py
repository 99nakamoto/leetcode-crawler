# -*- coding: utf-8 -*-

from setting_local import *


BOT_NAME = 'leetcode_crawler'

SPIDER_MODULES = ['leetcode_crawler.spiders']
NEWSPIDER_MODULE = 'leetcode_crawler.spiders'

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
# smaller is higher priority
ITEM_PIPELINES = {
   'leetcode_crawler.pipelines.LeetcodeCrawlerPipeline': 300,
   'leetcode_crawler.pipelines.MongodbPipeline': 900,
}

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY=5
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN=16
#CONCURRENT_REQUESTS_PER_IP=16

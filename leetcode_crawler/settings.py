# -*- coding: utf-8 -*-

BOT_NAME = 'leetcode_crawler'

SPIDER_MODULES = ['leetcode_crawler.spiders']
NEWSPIDER_MODULE = 'leetcode_crawler.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'leetcode_crawler (+http://www.yourdomain.com)'

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS=32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY=0
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN=16
#CONCURRENT_REQUESTS_PER_IP=16

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'leetcode_crawler.pipelines.LeetcodeCrawlerPipeline': 300,
}

MONGODB_SERVER = "45.54.133.34"
MONGODB_PORT = 27017
MONGODB_DB = "leetcode"
MONGODB_COLLECTION = "questions"

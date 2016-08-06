# -*- coding: utf-8 -*-

from setting_local import *


BOT_NAME = 'leetcode_crawler'

SPIDER_MODULES = ['leetcode_crawler.spiders']
NEWSPIDER_MODULE = 'leetcode_crawler.spiders'

ITEM_PIPELINES = {
   'leetcode_crawler.pipelines.LeetcodeCrawlerPipeline': 300,
}

DOWNLOAD_DELAY=5

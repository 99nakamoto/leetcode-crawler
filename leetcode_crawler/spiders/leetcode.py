from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy import Request

from leetcode_crawler.items import QuestionItem

import requests


# [deprecated]
class LeetcodeSpider(CrawlSpider):
    name = "leetcode"

    def start_requests(self):
        URL = "https://leetcode.com/problemset/algorithms/"
        # TODO: login my leetcode account here

        yield Request(URL, self.parse_list)

    def parse_list(self, response):
        # we check problem index range in here
        for trElement in response.xpath('//tbody[@class="reactable-data"]/tr'):

            # The ID of each question is checked against some predefined range
            # IDs are passed to callback as parameter, because item page does not contain ID number
            qUrl = trElement.xpath('td[3]/a/@href').extract()[0]
            qIndex = trElement.xpath('td[2]/text()').extract()[0]

            # TODO, there should be a better way to construct this url
            request = Request("https://leetcode.com" + qUrl,
                            callback=self.parse_item)
            request.meta['qIndex'] = int(qIndex)
            yield request

    def parse_item(self, response):
        item = QuestionItem()

        # TODO: also crawl the companies names
        item['index'] = str(response.meta['qIndex'])
        item['link'] = response.url
        item['content'] = response.xpath('//div[@class="question-content"]/*').extract()

        # temporarily omit the pages that need login
        # TODO: login my leetcode account here
        if not item['content']:
            return
        item['title'] = response.xpath('//div[@class="question-title"]/h3/text()').extract()[0]

        yield item

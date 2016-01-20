from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy import Request

from leetcode_crawler.items import QuestionItem

import requests

# leetcode login
# username3
# password3
# email@email.com

class LeetcodeSpider(CrawlSpider):
    name = "leetcode"

    def start_requests(self):
        URL = "https://leetcode.com/problemset/algorithms/"
        self.logger.info('start request at: %s', URL)
        # todo: did not do login here

        yield Request(URL, self.parse_list)

    def parse_list(self, response):
        self.logger.info('now parsing the list: %s', response.url)
        # we check problem index range in here
        for trElement in response.xpath('//tbody[@class="reactable-data"]/tr'):
            # The ID of each question is checked against some predefined range
            # IDs are passed to callback as parameter, because
            # the item page does not show a ID number
            qUrl = trElement.xpath('td[3]/a/@href').extract()[0]
            qIndex = trElement.xpath('td[2]/text()').extract()[0]

            request = Request(
                "https://leetcode.com" + qUrl,
                callback=self.parse_item
                )
            request.meta['qIndex'] = int(qIndex)
            yield request

    def parse_item(self, response):
        item = QuestionItem()

        item['index'] = str(response.meta['qIndex'])
        item['link'] = response.url
        item['content'] = response.xpath('//div[@class="question-content"]/*').extract()

        # there are somecases that page don't load when not logged in
        # omit these pages for now
        if not item['content']:
            return
        item['title'] = response.xpath('//div[@class="question-title"]/h3/text()').extract()[0]

        yield item

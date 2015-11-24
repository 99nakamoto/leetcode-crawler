from scrapy.http import FormRequest
from scrapy.spider import BaseSpider

import urllib2


class LoginSpider(BaseSpider):
    name = 'pinterest'
    start_urls = ['https://www.pinterest.com/login/']
    # you can set the user agent either in the settings or the spider
    user_agent = ('Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) '
                  'AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 '
                  'Mobile/9A334 Safari/7534.48.3')

    def parse(self, response):
        data = {'email': 'willran168@gmail.com', 'password': 'xxxxxxxxxxxxxxxxxxxxx'}
        # no need for dont_filter
        return FormRequest.from_response(response, formdata=data, 
            callback=self.after_login)

    def after_login(self, response):

        response = urllib2.urlopen('https://www.pinterest.com/settings/')
        html = response.read()
        file_ = open('result.html', 'w')
        file_.write(html)
        file_.close()

        print "================================" + response.url


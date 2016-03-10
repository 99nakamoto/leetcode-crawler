# -*- coding: utf-8 -*-

class LeetcodeCrawlerPipeline(object):
    def process_item(self, item, spider):

        # create a new file
        file_ = open(item['index'] + " " + item['title'] + '.html', 'w')

        # write the question information as HTML
        file_.write("<h1 style=\"font-family: Lucidatypewriter, monospace\">Question ")
        file_.write(item['index'] + ': ')
        file_.write(item['title'])
        file_.write("</h1>")
        file_.write('\n\n')

        file_.write('<a href="')
        file_.write(item['link'] + '">')
        file_.write(item['link'])
        file_.write("</a>")
        file_.write('\n\n')

        file_.write("<div style=\"font-family: Andale Mono, monospace\">")
        for line in item['content']:
            # if this line says: Subscribe to see which companies asked this question
            # skip this line
            if "to see which companies asked this question" in line:
                continue
            # convert all urls to absolute. there are cases like this:
            # src="/static/images/problemset/skyline1.jpg"
            # href="/problems/add-two-numbers/"
            # href="/tag/math/"
            line = line.encode('utf-8').replace('="/', '="http://leetcode.com/')
            file_.write(line + '\n')
        file_.write("</div>")

        file_.close()

        return item


class MongodbPipeline(object):

    def __init__(self):
        if (settings['SAVE_TO_MONGODB']):
            connection = pymongo.MongoClient(
                settings['MONGODB_SERVER'],
                settings['MONGODB_PORT']
            )
            db = connection[settings['MONGODB_DB']]
            self.collection = db[settings['MONGODB_COLLECTION']]

    def process_item(self, item, spider):
        if (settings['SAVE_TO_MONGODB']):
            self.collection.update(
                {'title': item['title']},
                dict(item), upsert=True
            )
            return item
        else:
            return item

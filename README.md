# This crawler is not under maintainance

This crawler is no longer under active maintainance. And it may not be working any more. 

Leetcode is no longer returning a static website, but instead, most of the conent is rendered at real time. 

If you have done this, another leetcode crawler, let me know and I'm happy to learn. 

# Note

[The below content is deprecated]

# leetcode-crawler

Web crawler that download unlocked questions from www.leetcode.com

## How to setup

You will need to install python, and Scrapy package.

1. https://www.python.org/
1. http://scrapy.org/

## How to configure

Modify the file: __settings.py__

	DOWNLOAD_DELAY=0

Change the value to 5 (recommended 5~10 seconds cooldown between each crawl).

## How to use

Go to main project directory and execute the following command:

    scrapy crawl leetcode

or execute with -o for an output file. 

# Save to MongoDB

The result of the crawler can be (optionally) saved to MongoDB by setting SAVE_TO_MONGODB to 1. 

The pipeline.py is used to do the connection + save the data. 

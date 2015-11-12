# leetcode-crawler
Simple web crawler that download all unlocked questions from leetcode.com 

## How to setup

You will need to install python, and Scrapy package.

1. https://www.python.org/
1. http://scrapy.org/

## How to configure

Modify the file: __settings.py__

	DOWNLOAD_DELAY=0

Change the value to 3 (recommended 3 seconds break between each crawl).

## How to use

Go to main project directory and execute the following command:

    scrapy crawl leetcode

If you use IPython, I suggest you execute: 

    !cls && scrapy crawl leetcode

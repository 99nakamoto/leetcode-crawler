# leetcode-crawler

Web crawler that download unlocked questions from leetcode.com 

## How to setup

You will need to install python, and Scrapy package.

1. https://www.python.org/
1. http://scrapy.org/

## How to configure

Modify the file: __settings.py__

	DOWNLOAD_DELAY=0

Change the value to 3 (recommended 3~10 seconds cooldown between each crawl).

## How to use

Go to main project directory and execute the following command:

    scrapy crawl leetcode

or execute with -o for an output file. 

# Save to MongoDB

The result of the crawler can be (optionally) saved to MongoDB by setting SAVE_TO_MONGODB to 1. 

The pipeline.py is used to do the connection + save the data. 

# -*- coding: utf-8 -*-

# Scrapy settings for spiders project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'spiders'

SPIDER_MODULES = ['spiders.spiders']
NEWSPIDER_MODULE = 'spiders.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'spiders (+http://www.yourdomain.com)'

#LOG_LEVEL = 'DEBUG'
CONCURRENT_REQUESTS = 1
DOWNLOAD_DELAY = 0.1
LOG_FILE = 'log.log'
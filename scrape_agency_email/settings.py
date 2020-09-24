# Scrapy settings for scrape_agency_email project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import os

BOT_NAME = 'scrape_agency_email'

SPIDER_MODULES = ['scrape_agency_email.spiders']
NEWSPIDER_MODULE = 'scrape_agency_email.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'scrape_agency_email (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

ROOT_DIR = os.getcwd()
SRC_DIR = os.path.join(ROOT_DIR, BOT_NAME, 'src')
BIN_DIR = os.path.join(ROOT_DIR, BOT_NAME, 'bin')

AGENCIES_CSV = 'agencies_export.csv'

GOOGLE_SEARCH_STRING = "https://www.google.com/search?sxsrf=ALeKk03buSv2rHpGi1uDdfDaYVSZtWbp6w%3A1600890594273&source" \
                       "=hp&ei=4qZrX5eODtDClwTQ9JLICA&q={0}&oq={0}&gs_lcp" \
                       "=CgZwc3ktYWIQAzILCC4QxwEQrwEQkwIyBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeOgcIIxDqAhAnUNsJWNsJYI4QaAFwAHgAgAGeAYgBngGSAQMwLjGYAQCgAQKgAQGqAQdnd3Mtd2l6sAEK&sclient=psy-ab&ved=0ahUKEwiXh8aZhoDsAhVQ4YUKHVC6BIkQ4dUDCAc&uact=5 "

SELENIUM_DRIVER = os.path.join(BIN_DIR, 'chromedriver')
HEALTH_DIRECT_URL = "https://www.healthdirect.gov.au/australian-health-services?tab=byname&pageIndex=1&practiceName={}"

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'scrape_agency_email.middlewares.ScrapeAgencyEmailSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'scrape_agency_email.middlewares.ScrapeAgencyEmailDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'scrape_agency_email.pipelines.ScrapeAgencyEmailPipeline': 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

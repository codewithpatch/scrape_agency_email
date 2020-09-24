import os

BOT_NAME = 'scrape_agency_email'

SPIDER_MODULES = ['scrape_agency_email.spiders']
NEWSPIDER_MODULE = 'scrape_agency_email.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False


ROOT_DIR = os.getcwd()
SRC_DIR = os.path.join(ROOT_DIR, BOT_NAME, 'src')
BIN_DIR = os.path.join(ROOT_DIR, BOT_NAME, 'bin')
LOG_DIR = os.path.join(ROOT_DIR, BOT_NAME, 'logs')
OUT_DIR = os.path.join(ROOT_DIR, BOT_NAME, 'output')

# LOGS
LOG_LEVEL = 'INFO'
LOG_FORMAT = '%(levelname)s: %(message)s'
# LOG_FILE = os.path.join(LOG_DIR, 'runlogs.log')

AGENCIES_CSV = 'agencies_export.csv'

GOOGLE_SEARCH_STRING = "https://www.google.com/search?sxsrf=ALeKk03buSv2rHpGi1uDdfDaYVSZtWbp6w%3A1600890594273&source" \
                       "=hp&ei=4qZrX5eODtDClwTQ9JLICA&q={0}&oq={0}&gs_lcp" \
                       "=CgZwc3ktYWIQAzILCC4QxwEQrwEQkwIyBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeOgcIIxDqAhAnUNsJWNsJYI4QaAFwAHgAgAGeAYgBngGSAQMwLjGYAQCgAQKgAQGqAQdnd3Mtd2l6sAEK&sclient=psy-ab&ved=0ahUKEwiXh8aZhoDsAhVQ4YUKHVC6BIkQ4dUDCAc&uact=5 "

SELENIUM_DRIVER = os.path.join(BIN_DIR, 'chromedriver')
HEALTH_DIRECT_URL = "https://www.healthdirect.gov.au/australian-health-services?tab=byname&pageIndex=1&practiceName={}"

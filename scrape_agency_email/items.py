# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from pandas import DataFrame


class ScrapeAgencyEmailItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    agency_df: DataFrame = scrapy.Field()

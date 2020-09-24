import os
import re
from typing import Generator

import scrapy
import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from more_itertools import unique_everseen
from pandas import DataFrame
from scrapy.utils.project import get_project_settings
from scrapy.utils.response import open_in_browser

from ..scrapy_selenium import ScrapySelenium


class SpiderSpider(scrapy.Spider):
    name = 'spider'
    settings = get_project_settings()

    def __init__(self, page_url='', url_file=None, *args, **kwargs):
        self.__start_selenium_process()

        self.start_urls = [
            self.__generate_search_url(agency_name)
            for agency_name in self.agency_names_without_email
        ]

        if not page_url and url_file is None:
            TypeError('No page URL or URL file passed.')

        if url_file is not None:
            with open(url_file, 'r') as f:
                self.start_urls = f.readlines()
        if page_url:
            # Replaces the list of URLs if url_file is also provided
            self.start_urls = [page_url]

        super().__init__(*args, **kwargs)

    @property
    def agencies_csv(self) -> str:
        SRC_DIR = self.settings.get('SRC_DIR')
        csv_filename = self.settings.get('AGENCIES_CSV')
        return os.path.join(SRC_DIR, csv_filename)

    @property
    def agency_df(self) -> DataFrame:
        agencies_df = pd.read_csv(self.agencies_csv)

        return agencies_df

    @property
    def agency_names_without_email(self) -> Generator[str, None, None]:
        for agency_name, email in zip(self.agency_df.name, self.agency_df.email):
            if str(email) != 'nan':
                continue

            yield agency_name

    def __start_selenium_process(self):
        selenium_process = ScrapySelenium(self.agency_names_without_email)
        selenium_process.main()
        pass

    def __generate_search_url(self, search_string):
        search_string_replace = search_string.replace(" ", "+")

        google_search_url = self.settings.get("GOOGLE_SEARCH_STRING").format(search_string_replace)
        return google_search_url

    def start_requests(self):
        for page in self.start_urls:
            yield scrapy.Request(url=page, callback=self.crawl_google_search)

    def crawl_google_search(self, response):
        open_in_browser(response)
        google_search_result_urls = response.xpath('//div[@class="kCrYT"]//@href').getall()
        possible_agency_urls = self.__clean_google_search_result(google_search_result_urls)
        filtered_possible_urls = list(filter(self.__is_possible_agency_url, possible_agency_urls))
        filtered_possible_urls = list(unique_everseen(filtered_possible_urls))
        # TODO: Skip if hotdoc.com.au is first in the list of url
        # TODO: Check if healthdirect.gov.au can help search directories
        return

    def __clean_google_search_result(self, search_results: list) -> list:
        regex = re.compile(r"https?://.*?(\.org)?(\.com)?(\.au)?/", re.I)
        regex_matches = list(map(regex.search, search_results))
        result_urls = [match.group(0) for match in regex_matches]

        return result_urls

    def __is_possible_agency_url(self, url: str) -> bool:
        if "maps.google" in url:
            return False

        if 'facebook' in url:
            return False

        if 'linkedin' in url:
            return False

        if 'youtube' in url:
            return False

        if 'moovitapp' in url:
            return False

        if 'google' in url:
            return False

        if 'wikipedia' in url:
            return False

        if url.endswith(".au/"):
            return True

        if url.endswith(".com/"):
            return True

        if url.endswith(".net/"):
            return True

        if url.endswith(".org/"):
            return True

        if url.endswith(".co/"):
            return True

        if url.endswith(".nz/"):
            return True

        if url.endswith(".uk/"):
            return True

        return False

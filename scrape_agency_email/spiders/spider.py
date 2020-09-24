import logging
import os
from typing import Generator

import pandas as pd
import scrapy
from pandas import DataFrame
from scrapy.utils.project import get_project_settings

from ..models import AgencyScrapedDetails
from ..scrapy_selenium import ScrapySelenium


class SpiderSpider(scrapy.Spider):
    name = 'spider'
    settings = get_project_settings()

    def __init__(self, page_url='', url_file=None, *args, **kwargs):
        self.__start_selenium_process()

        self.start_urls = []

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
        logging.info("Starting Selenium Process")
        selenium_process = ScrapySelenium(self.agency_names_without_email)
        scrape_from_health_direct = selenium_process.main()

        df = self.agency_df
        for scraped_data in scrape_from_health_direct:
            df.loc[df.name == scraped_data.agency_name, 'email'] = scraped_data.agency_email

        self.__write_agency_df_to_csv(df)

    def __add_to_agency_df(self, df, data: AgencyScrapedDetails) -> None:
        df.loc[df.name == data.agency_name, 'email'] = data.agency_email

    def __write_agency_df_to_csv(self, df: DataFrame) -> None:
        output_dir = self.settings.get("OUT_DIR")
        path = os.path.join(output_dir, 'Agencies3.csv')
        df.to_csv(path, index=False, header=True)

    def __generate_search_url(self, search_string):
        search_string_replace = search_string.replace(" ", "+")

        google_search_url = self.settings.get("GOOGLE_SEARCH_STRING").format(search_string_replace)
        return google_search_url

import logging
import time
from typing import Iterable

from bs4 import BeautifulSoup
from scrapy.utils.project import get_project_settings
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


class ScrapySelenium:
    settings = get_project_settings()

    def __init__(self, agency_names: Iterable[str]):
        self.agency_names = agency_names

        self.driver = webdriver.Chrome(executable_path=self.chrome_driver, options=self.selenium_option)

    def main(self):
        for agency_name in self.agency_names:
            converted_agency_name = self.__convert_agency_name(agency_name, sep="-")
            search_url = self.directory_raw_url.format(converted_agency_name)

            self.driver.get(search_url)

            while True:
                '''
                Wait for the result to load before getting
                agency url
                '''
                logging.debug("Waiting for result to show in the search page...")
                if "<h2>Medical centers</h2>" not in self.driver.page_source:
                    continue

                if "No medical centres found" in self.driver.page_source:
                    logging.warning(f"No medical centres found for {agency_name}")
                    break

                if "<h2>Medical centers</h2>" in self.driver.page_source:
                    result = self.__try_get_agency_url(agency_name)
                    break




            continue

    def __try_get_agency_url(self, agency_name):
        """
        "No medical centres found matching the criteria. Please try with a different search combination."
        in self.driver.page_source

        div id=divResultsContainer

        page_source = self.driver.page_source
        soup = BeautifulSoup(page_source, 'lxml')
        result_container = soup.find('div', attrs={'id': 'divResultsContainer'})
        children = list(result_container.children)
        """
        while True:
            soup = BeautifulSoup(self.driver.page_source, 'lxml')
            result_container = soup.find('div', attrs={'id': 'divResultsContainer'})
            if not result_container.text:
                continue

            children = list(result_container.children)
            if not children:
                logging.warning(f"No children found in result container for {agency_name}")
                return None

            text_result = children[0].text.strip()
            result_xpath = '//*[@id="divResultsContainer"]/a'
            if len(children) > 1:
                result_xpath = '//*[@id="divResultsContainer"]/a[1]'

            try:
                result_position = self.driver.find_element_by_xpath(result_xpath)
                result_position.click()

                while True:
                    # Check if the next url already loads
                    if "Services Available" in self.driver.page_source:
                        email = self.__parse_email_from_url()

                        return email

                break
            except Exception:
                continue

    def __parse_email_from_url(self):
        soup = BeautifulSoup(self.driver.page_source, 'lxml')
        contact_container = soup.find('div', attrs={"class": "veyron-hsf-contact-details"})

        try:
            email = contact_container.attrs['data-email']
            if email == 'null':
                logging.warning("No email found in the agency website!")
                return None

            return email
        except KeyError:
            logging.warning("No email found in the agency website!")
            return None

    @property
    def chrome_driver(self):
        return self.settings.get("SELENIUM_DRIVER")

    @property
    def selenium_option(self):
        option = Options()
        prefs = {"profile.default_content_setting_values.notifications": 2}
        option.add_argument('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                            'Chrome/84.0.4147.89 Safari/537.36')
        option.add_experimental_option("prefs", prefs)
        option.add_argument("start-maximized")
        option.add_argument("--disable-infobars")
        option.add_argument("--disable-extensions")

        return option

    @property
    def directory_raw_url(self):
        return self.settings.get("HEALTH_DIRECT_URL")

    @staticmethod
    def __convert_agency_name(agency_name, sep):
        agency_name_split = agency_name.split(" ")
        return sep.join(agency_name_split)

    def close_selenium(self):
        self.driver.quit()


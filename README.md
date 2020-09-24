# scrape_agency_email

## Description
This project goals to scrape agency email from a list of agency names.

## Dependencies
1. Install the following dependencies from requirements.txt
    `pip install -r requirements.txt`
    
## ChromeDriver
1. The development of this script is using chromedriver84 version for mac.
2. Check your chrome version in the about page of chrome.
3. Download your corresponding chromedriver version in chromedrier website https://chromedriver.chromium.org/downloads
4. Make sure to download the chromedriver version corresponding to your OS(Mac, Windows, Linux)

## Logging to File
1. In `settings.py`, uncomment line 21 to output your logs in the log directory.
2. LOG Directory -> `scrape_agency_email/logs/`

## Output file
1. CSV  -> `scrape_agency_email/output/Agencies3.csv`

## Running the script
1. From the root directory, run:
```
scrapy crawl spider
```


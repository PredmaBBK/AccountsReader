# This file works with the UI to return the companies from a given search string and the years for which their accounts are available.
# Additionally, it downloads the selected accounting files when they have been chosen by the user.

# Install dependencies. Apply settings for the selenium webdriver.
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time
options = Options()
options.add_experimental_option('prefs', {
"download.default_directory": "/Users/predm/OneDrive/Documents/Birkbeck/MSc Project/Python practice/AccountsTemp", #Change default directory for downloads
"download.prompt_for_download": False, #To auto download the file
"download.directory_upgrade": True,
"plugins.always_open_pdf_externally": True #It will not show PDF directly in chrome
})
options.add_argument("--headless")
driver = webdriver.Chrome(options= options)

# Functionality to return the top list of company names from the user's request.
# This is returned as a list of pairs of company names and their links
def company_search_results(company_string):
    company_string = company_string.replace(' ', '+')
    search_string = "https://find-and-update.company-information.service.gov.uk/search?q=" + company_string
    driver.get(search_string)

    mainResults = driver.find_element(By.ID, "services-information-results")
    companies = mainResults.find_elements(By.CLASS_NAME, "type-company")

    links = []
    for company in companies:

        h3 = company.find_element(By.CSS_SELECTOR, "h3")
        a = h3.find_element(By.CSS_SELECTOR, "a")
        link = a.get_attribute("href") + "/filing-history"
        company_pair = [a.text, link]

        links.append(company_pair)

    return links


# Functionality to download and save the PDFs for those companies.

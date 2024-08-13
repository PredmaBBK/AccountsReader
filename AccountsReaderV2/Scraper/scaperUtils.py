#This file provides some helper methods for the scaper script

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

options.add_argument("--headless")



def convert_to_download_links(links):
    for link in links:
        link.replace("download=0", "download=1")
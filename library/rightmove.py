from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from library.scrapper import Scrapper
import pandas as pd
import time

class RightmoveScrapper(Scrapper):
    def __init__(self, url: str = 'https://www.rightmove.co.uk/', headless: bool = False):
        super().__init__(url, headless)

    def search_property(self,
                        property: str,
                        xpath_search_bar: str = '//input[@class="ksc_inputText ksc_typeAheadInputField"]'):
        self.accept_cookies()

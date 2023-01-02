from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

class Scrapper:

    def __init__(self, url: str, headless: bool):
        if headless:
            chrome_options = Options()
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--windows-size=1920,1080")
            chrome_options.add_argument("--start-maximized")
            self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
        else:
            self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get(url)

    def click_element(self, xpath: str):
        '''
        Find and click "Accept Cookie" button

        Parameters
        ----------
        xpath: str
            The xPath of the element to be clicked
        '''
        element = self.driver.find_element(By.XPATH, xpath)
        element.click()

    def accept_cookies(self, xpath = '//button[@class="optanon-allow-all accept-cookies-button"]'):
        '''
        Find and click the "Accept Cookies" button
        
        Parameters
        ----------
        xpath: str
            The xpath of the Accept Cookies button
        '''
        self.click_element(xpath)

    def find_elements_in_container(self, xpath_container: str, tag_elements: str, direct_child: bool = True) -> list:
        '''
        Find a container and return a list of elements inside it
        
        Parameter
        ---------
        xpath_container: str
            The xpath of the container
        tag_elements: str
            The tag of the elements to be found
        direct_child: bool
            If True, the elements will be found directly inside the container,
            otherwise, they will be found inside the container's children
        '''
        container = self.driver.find_element(By.XPATH, xpath_container)
        if direct_child:
            elements_in_container = container.find_elements(By.XPATH, f'./{tag_elements}')
        else:
            elements_in_container = container.find_elements(By.XPATH, f'.//{tag_elements}')
        return elements_in_container
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from consts import *


class Selenium:
    def __init__(self):
        options = Options()
        # options.add_argument("--headless")  # Runs Chrome in headless mode.
        options.add_argument('--no-sandbox')  # Bypass OS security model
        options.add_argument('--disable-gpu')  # applicable to windows os only
        options.add_argument('start-maximized')  #
        options.add_argument('disable-infobars')
        options.add_argument("--disable-extensions")
        self.driver = webdriver.Chrome(chrome_options=options, executable_path=CHROMEDRIVER_PATH)

    def launch_chrome(self):
        self.driver.get(BASE_URL)
        self.driver.implicitly_wait(3)

    def go_to_decleration_page(self):
        self.driver.find_element_by_xpath(DECLERATION_LINK).click()
        self.driver.set_page_load_timeout(20)

    def login(self, username, password):
        self.driver.find_element_by_id(BLOCKER).click()
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_id(USERNAME).send_keys(username)
        self.driver.find_element_by_id(PASSWORD).send_keys(password)
        self.driver.find_element_by_id(LOGIN_BUTTON).click()
        self.driver.set_page_load_timeout(20)

    def quit(self):
        self.driver.quit()
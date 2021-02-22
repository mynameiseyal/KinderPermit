import time
from datetime import datetime
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from consts import *

path = Path(__file__).parent
today = datetime.today().strftime('%d-%m-%Y')


class Selenium:
    def __init__(self):
        options = Options()
        # options.add_argument("--headless")  # Runs Chrome in headless mode.
        options.add_argument('--no-sandbox')  # Bypass OS security model
        options.add_argument('--disable-gpu')  # applicable to windows os only
        options.add_argument('start-maximized')  #
        options.add_argument('disable-infobars')
        options.add_argument("--disable-extensions")
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=options)
        # self.driver = webdriver.Chrome(chrome_options=options, executable_path=CHROMEDRIVER_PATH)

    def launch_chrome(self):
        self.driver.get(BASE_URL)
        time.sleep(10)

    def go_to_decleration_page(self):
        page_buttons = self.driver.find_elements_by_xpath(DECLERATION_PAGE_BUTTONS)
        page_buttons[1].click()  # Second button, go to login page
        time.sleep(10)

    def login(self, username, password):
        self.driver.find_element_by_id(BLOCKER).click()
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_id(USERNAME).send_keys(username)
        self.driver.find_element_by_id(PASSWORD).send_keys(password)
        self.driver.find_element_by_id(LOGIN_BUTTON).click()
        time.sleep(10)

    def sign_health_decleration(self):
        # First decleration:
        self.driver.find_element_by_xpath(FIRST_DEC_EXPAND).click()
        time.sleep(5)
        self.driver.find_element_by_xpath(FIRST_DEC_APPROVE).click()
        time.sleep(7)
        self.driver.refresh()
        time.sleep(5)
        # Second decleration:
        self.driver.find_element_by_xpath(SECOND_DEC_EXPAND).click()
        time.sleep(5)
        self.driver.find_element_by_xpath(SECOND_DEC_APPROVE).click()
        time.sleep(7)
        self.driver.refresh()
        time.sleep(10)

    def go_out_and_in_to_decleration_page(self):
        self.driver.get(GOOGLE_URL)
        time.sleep(3)
        self.driver.get(BASE_URL)
        time.sleep(10)


    def save_screenshot(self):
        # self.driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
        screenshot = f"ISHUR_{today}.png"
        self.driver.refresh()
        time.sleep(5)
        self.driver.get_screenshot_as_file(screenshot)
        return screenshot

    def delete_file(self):
        file_name = f"ISHUR_{today}.png"
        for filename in path.iterdir():
            if filename.is_file():
                if filename.name == file_name:
                    filename.unlink()

    def quit(self):
        self.delete_file()
        self.driver.quit()
        time.sleep(10)
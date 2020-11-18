import time
from datetime import datetime
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
        time.sleep(7)

    def sign_health_decleration(self):
        # First decleration:
        self.driver.find_element_by_xpath(FIRST_DEC_EXPAND).click()
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, FIRST_DEC_APPROVE)))
        self.driver.find_element_by_xpath(FIRST_DEC_APPROVE).click()
        # Second decleration:
        self.driver.find_element_by_xpath(SECOND_DEC_EXPAND).click()
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, SECOND_DEC_APPROVE)))
        # time.sleep(3)
        self.driver.find_element_by_xpath(SECOND_DEC_APPROVE).click()
        time.sleep(7)

    def save_screenshot(self):
        screenshot = f"ISHUR_{today}.png"
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
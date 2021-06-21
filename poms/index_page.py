from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class IndexPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def login(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "login")))

    def username_input(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "usernameInput")))

    def password_input(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "passwordInput")))

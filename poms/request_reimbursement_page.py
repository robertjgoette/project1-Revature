from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class RequestReimbursement:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def amount_input(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "amountInput")))

    def message_input(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "messageInput")))

    def send_reimbursement_button(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "sendReimbursement")))

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class EmployeePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def request_reimbursement(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "requestReimbursement")))

    def log_out(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "logOut")))

    def stat_button(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "statButton")))

    def reimbursement_response(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "reimbursementResponse")))

    def pending_tab(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "pendingBox")))

    def approve_button1(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "approve3")))

    def approve_button2(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "reimbursementResponseSumitApprove")))

    def deny_button1(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "deny5")))

    def deny_button2(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "reimbursementResponseSumitDeny")))

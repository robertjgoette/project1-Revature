from behave.runner import Context
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from poms.index_page import IndexPage
from poms.employee_page import EmployeePage
from poms.request_reimbursement_page import RequestReimbursement
from poms.statistics_page import StatisticsPage


def before_all(context: Context):
    context.driver: WebDriver = webdriver.Chrome(
        'C:\\Users\\Robby Goette\\Desktop\\Revature\\chromedriver_win32\\chromedriver.exe')
    context.index_page = IndexPage(context.driver)
    context.employee_page = EmployeePage(context.driver)
    context.request_reimbursement_page = RequestReimbursement(context.driver)
    context.statistics_page = StatisticsPage(context.driver)


def after_all(context):
    context.driver.quit()

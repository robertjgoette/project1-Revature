import time
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


@given(u'The employee is on the login screen')
def step_impl(context):
    context.driver.get(
        "C:\\Users\\Robby Goette\\PycharmProjects\\project_1_expense_reimbursement_system\\html\\index.html")


@when(u'The employee enters their username into the username input')
def step_impl(context):
    context.index_page.username_input().send_keys("Hexgonagiveit")


@when(u'The employee enters their password into the password input')
def step_impl(context):
    context.index_page.password_input().send_keys("hex")


@when(u'The employee clicks on login')
def step_impl(context):
    time.sleep(1)
    context.index_page.login().click()


@then(u'The employee should be redirected to Employee page')
def step_impl(context):
    time.sleep(1)
    home_title = context.driver.title
    assert home_title == "Employee Page"


@given(u'The employee is on the Employee front page')
def step_impl(context):
    context.driver.get(
        "C:\\Users\\Robby Goette\\PycharmProjects\\project_1_expense_reimbursement_system\\html\\employee_page.html")


@when(u'The employee clicks on the Request Reimbursement button')
def step_impl(context):
    time.sleep(1)
    context.employee_page.request_reimbursement().click()


@then(u'The employee is redirected to request reimbursement page')
def step_impl(context):
    title = context.driver.title
    print(title)
    assert title == "Request Reimbursement"


@when(u'The employee enters the amount into the amount input')
def step_impl(context):
    context.request_reimbursement_page.amount_input().send_keys("255")


@when(u'The employee enters their message into the message input')
def step_impl(context):
    context.request_reimbursement_page.message_input().send_keys(" Beep Boop I am a Robot.")


@when(u'The employee clicks on submit reimbursement')
def step_impl(context):
    time.sleep(1)
    context.request_reimbursement_page.send_reimbursement_button().click()


@then(u'The employee is redirected to the Employee page')
def step_impl(context):
    WebDriverWait(context.driver, 5).until(EC.presence_of_element_located((By.ID, "requestReimbursement")))
    title = context.driver.title
    assert title == "Employee Page"


@when(u'The employee clicks on the Logout button')
def step_impl(context):
    time.sleep(1)
    context.employee_page.log_out().click()


@then(u'The employee is redirected to index page')
def step_impl(context):
    time.sleep(1)
    title = context.driver.title
    assert title == "Login"

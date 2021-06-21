import time

from behave import given, when, then


@given(u'The manager is on the login screen')
def step_impl(context):
    context.driver.get(
        "C:\\Users\\Robby Goette\\PycharmProjects\\project_1_expense_reimbursement_system\\html\\index.html")


@when(u'The manager enters their username into the username input')
def step_impl(context):
    context.index_page.username_input().send_keys("lonelymountainking")


@when(u'The manager enters their password into the password input')
def step_impl(context):
    context.index_page.password_input().send_keys("heartofthemountain")


@when(u'The manager clicks on login')
def step_impl(context):
    time.sleep(1)
    context.index_page.login().click()


@then(u'The manager should be redirected to Employee page')
def step_impl(context):
    time.sleep(1)
    home_title = context.driver.title
    assert home_title == "Employee Page"


@given(u'The manager is on the Employee front page')
def step_impl(context):
    context.driver.get(
        "C:\\Users\\Robby Goette\\PycharmProjects\\project_1_expense_reimbursement_system\\html\\employee_page.html")

@when (u'The manager clicks on the pending box')
def step_impl(context):
    time.sleep(1)
    context.employee_page.pending_tab().click()

@when(u'The manager clicks on a approve button')
def step_impl(context):
    time.sleep(1)
    context.employee_page.approve_button1().click()


@when(u'The manager enters a response into the Response input')
def step_impl(context):
    context.employee_page.reimbursement_response().send_keys("I have read this request.")


@when(u'The manager clicks on Reimbursement Response Submit Approve button')
def step_impl(context):
    time.sleep(1)
    context.employee_page.approve_button2().click()


@then(u'The manager is redirected to the Employee page')
def step_impl(context):
    time.sleep(1)
    home_title = context.driver.title
    assert home_title == "Employee Page"


@when(u'The manager clicks on a deny button')
def step_impl(context):
    time.sleep(1)
    context.employee_page.deny_button1().click()


@when(u'The manager clicks on Reimbursement Response Submit Deny button')
def step_impl(context):
    time.sleep(1)
    context.employee_page.deny_button2().click()


@when(u'The manager clicks on the Statistics button')
def step_impl(context):
    time.sleep(1)
    context.employee_page.stat_button().click()


@then(u'The manager is redirected to Statistics page')
def step_impl(context):
    time.sleep(1)
    home_title = context.driver.title
    assert home_title == "Statistics"


@when(u'The manager clicks on the Back To Home button')
def step_impl(context):
    context.statistics_page.back_to_home().click()


@when(u'The manager clicks on the Logout button')
def step_impl(context):
    time.sleep(1)
    context.employee_page.log_out().click()


@then(u'The manager is redirected to index page')
def step_impl(context):
    time.sleep(1)
    title = context.driver.title
    assert title == "Login"

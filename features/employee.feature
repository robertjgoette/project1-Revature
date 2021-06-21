Feature: An employee should be able to use their account

  Scenario:Login into my account
    Given The employee is on the login screen
    When The employee enters their username into the username input
    When The employee enters their password into the password input
    When The employee clicks on login
    Then The employee should be redirected to Employee page

  Scenario:Submit a reimbursement
    Given The employee is on the Employee front page
    When The employee clicks on the Request Reimbursement button
    Then The employee is redirected to request reimbursement page
    When The employee enters the amount into the amount input
    When The employee enters their message into the message input
    When The employee clicks on submit reimbursement
    Then The employee is redirected to the Employee page

  Scenario:Logout of my account
    Given The employee is on the Employee front page
    When The employee clicks on the Logout button
    Then The employee is redirected to index page

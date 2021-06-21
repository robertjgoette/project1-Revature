Feature: A manager should be able to view employees request and interact with them

  Scenario:Login into my account
    Given The manager is on the login screen
    When The manager enters their username into the username input
    When The manager enters their password into the password input
    When The manager clicks on login
    Then The manager should be redirected to Employee page

  Scenario:Approve a reimbursement
    Given The manager is on the Employee front page
    When The manager clicks on the pending box
    When The manager clicks on a approve button
    When The manager enters a response into the Response input
    When The manager clicks on Reimbursement Response Submit Approve button
    Then The manager is redirected to the Employee page

  Scenario:Deny a reimbursement
    Given The manager is on the Employee front page
    When The manager clicks on the pending box
    When The manager clicks on a deny button
    When The manager enters a response into the Response input
    When The manager clicks on Reimbursement Response Submit Deny button
    Then The manager is redirected to the Employee page

  Scenario:See Statistics Page
    Given The manager is on the Employee front page
    When The manager clicks on the Statistics button
    Then The manager is redirected to Statistics page
    When The manager clicks on the Back To Home button
    Then The manager is redirected to the Employee page

  Scenario:Logout of my account
    Given The manager is on the Employee front page
    When The manager clicks on the Logout button
    Then The manager is redirected to index page
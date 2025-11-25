Feature: Login Feature

  Scenario: Valid Login
    Given I navigate to the login page
    When I enter valid username and password
    And I click on login button
    Then I should see dashboard page

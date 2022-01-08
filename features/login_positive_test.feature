Feature: Login Testcase

  Scenario: Login Valid
    Given I navigate to "https://ralali.com/login"
    Then I fill email field using "jambhu@protonmail.com"
    Then I fill password field using "ralalidotcom"
    When I click Login
    And I see text "Jambu" on page
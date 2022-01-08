Feature: Login Testcase

  Scenario: Login Invalid
    Given I navigate to "https://ralali.com/login"
    Then I fill email field using "emailnya@email.com"
    Then I fill password field using "passwordnya"
    When I click Login
    And I see text "Belum Terdaftar" on page
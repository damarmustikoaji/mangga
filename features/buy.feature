Feature: Buy Testcase

  Scenario: Login
    Given I navigate to "https://dev.ralali.xyz"
    When I click Login
    Then I fill email field using "damar.aji@ralali.com"
    Then I fill password field using "12345678"
    And I see text "Hi, Damar Mustiko A.." on page

  Scenario: Buy a Product
    #Given I navigate to "https://dev.ralali.xyz/show-cart"
    Given I navigate to "https://dev.ralali.xyz/v/ocistore/product/Kerupuk-kulit"
    When I click Buy
    Then I see the Shopping Cart
    Then I click Continue to checkout
    Then I click Continue with shipping
    Then I see text "WAHANA" on page
    And I choose payment method using "Credit Card"
    Given I waiting for "10" seconds
    Then I fill number Credit Card

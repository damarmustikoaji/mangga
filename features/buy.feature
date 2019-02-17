Feature: Login

  Scenario: Login Valid
    Given I navigate to "https://dev.ralali.xyz/"
    When I click Login
    Then I fill email field using "damar.aji@ralali.com"
    Then I fill password field using "12345678"
    And I see a home page "Hi, Damar Mustiko A.."

  Scenario: Wallet Activation
    Given I waiting for "10" seconds
    When I see the Wallet Activation
    And I click "Later" for Wallet Activation

  Scenario: Share Promo Code
    When I see the Promo Share Modal
    Then I click Close Promo

  Scenario: Search Home Page
    Then I search for "Tekiro"
    When I am taken to the "Tekiro" Search Results page
    And I see a search result "TEKIRO Selang Recoil Kuning 6M type 15M"

  Scenario: Buy Product
    Given I buy product "TEKIRO Selang Recoil Kuning 6M type 15M"
    When I see the Shopping Cart
    Then I click Checkout
    And I waiting for "10" seconds

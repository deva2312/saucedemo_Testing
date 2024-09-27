@swacedemo
Feature: Login checks and product Ordering

  @Successful_Login
  Scenario: 1 Successful Login
    Given I am on the Demo Login Page
    When I fill the account information for account StandardUser into the Username field and the Password field
    And  I click the Login Button
    Then I am redirected to the Demo Main
    Then I verify the App Logo exists


  @Failed_Login
  Scenario: 2 Failed Login
    Given I am on the Demo Login Page
    When I fill the account information for account LockedOutUser into the Username field and the Password field
    And I click the Login Button
    Then I verify the Error Message Contains the text "Epic sadface: Sorry, this user has been locked out."


   @Ordering_a_high_price_Product
   Scenario: 3 Order a Product
    Given I am on the inventory Page
    When user sorts products from high price to low price
    And user adds highest Priced product
    And user clicks on cart
    And user clicks on Checkout
    And user enters first name Alice
    And user enters last name Doe
    And user enters zip code 592
    And user clicks Continue button
    Then I verify in checkout overview page if the total amount for the added item is $49.99
    When user clicks Finish button
    Then Thank you header is shown in checkout complete page
Feature: Login

Scenario: A valid user logs in to Google
    Given the Google homepage is displayed
    When the sign in button is pressed
    And valid user credentials are entered
    Then the Google homepage is displayed
    And an icon in the top right displays the logged in user
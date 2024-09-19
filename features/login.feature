Feature: Candidate CV Upload

  Scenario: User uploads a valid CV with the pre-fill feature enabled
    Given the user is on the login page
    When the user logs in with email "lorismaeshielda@gmail.com" and password "*Arcilla00"
    And the user selects a valid CV file to upload on the profile page
    Then the user should see the pre-filled data on the experience and skills page

  Scenario: User uploads an invalid CV with the pre-fill feature enabled
    Given the user is on the login page
    When the user logs in with email "lorismaeshielda@gmail.com" and password "*Arcilla00"
    And the user selects an invalid CV file to upload on the profile page
    Then an error message should be displayed indicating the upload failed
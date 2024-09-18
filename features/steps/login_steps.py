from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from pages.experience_skills_page import ExperienceSkillsPage
import time

@given('the user is on the login page')
def step_open_login_page(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://candidate-qa-test.dev.platform.compono.dev/")
    context.driver.maximize_window()
    time.sleep(5)

@when('the user logs in with email "{email}" and password "{password}"')
def step_login(context, email, password):
    login_page = LoginPage(context.driver)
    login_page.enter_email(email)
    login_page.enter_password(password)
    login_page.click_login()
    time.sleep(5)

@when('the user selects a valid CV file to upload on the profile page')
def step_upload_valid_cv(context):
    time.sleep(5)
    profile_page = ProfilePage(context.driver)
    button_field = context.driver.find_element(By.XPATH, "//button[@data-testid='upload-cv-button']")
    print(f"Button text: {button_field.text}")
    button_text = button_field.text

    if button_text == "Update your CV":
        profile_page.update_cv()
        time.sleep(5)
        profile_page.upload_valid_cv()
        time.sleep(15)
    else:
        profile_page.upload_valid_cv()
        time.sleep(15)

@when('the user selects an invalid CV file to upload on the profile page')
def step_upload_invalid_cv(context):
    time.sleep(5)
    profile_page = ProfilePage(context.driver)
    button_field = context.driver.find_element(By.XPATH, "//button[@data-testid='upload-cv-button']")
    print(f"Button text: {button_field.text}")
    button_text = button_field.text
    if button_text == "Update your CV":
        profile_page.update_cv()
        time.sleep(5)
        profile_page.upload_invalid_cv()
        time.sleep(15)
    else:
        profile_page.upload_invalid_cv()
        time.sleep(15)

@then('the user should see the pre-filled data on the experience and skills page')
def step_verify_prefilled_data(context):
    # Navigate to Experience and Skills page
    context.driver.get("https://candidate-qa-test.dev.platform.compono.dev/profile/experience-and-skills/")
    time.sleep(10)
    experience_page = ExperienceSkillsPage(context.driver)
    try:
        assert experience_page.get_new_job_details() is None, "Test Failed: No experience and skills found."
    except NoSuchElementException:
        count = len(experience_page.get_pre_filled_data())
        print(f"Number of experience and skills found: {count}")

@then('an error message should be displayed indicating the upload failed')
def step_verify_error_message(context):
    upload_failed = context.driver.find_element(By.XPATH, "//div[@class='sc-iujRgT DUXry']")
    upload_failed_message = upload_failed.text
    error_details = context.driver.find_element(By.CSS_SELECTOR, ".sc-iujRgT.DUXry small")
    error_details_message = error_details.text
    assert "Upload fail" in upload_failed_message, "Upload fail not found."
    assert "is not an accepted file type" in error_details_message, "Invalid file type message not found."
    print("Test Passed: Upload failure has been correctly detected.")

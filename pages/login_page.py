import time

from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_email(self, email):
        email_field = self.driver.find_element(By.ID, "1-email")
        time.sleep(1)
        email_field.clear()
        email_field.send_keys(email)
        time.sleep(2)

    def enter_password(self, password):
        password_field = self.driver.find_element(By.NAME, "password")
        time.sleep(1)
        password_field.clear()
        password_field.send_keys(password)
        time.sleep(2)

    def click_login(self):
        login_button = self.driver.find_element(By.NAME, "submit")
        time.sleep(1)
        login_button.click()
        time.sleep(2)

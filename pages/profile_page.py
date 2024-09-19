from selenium.webdriver.common.by import By
import os

class ProfilePage:
    def __init__(self, driver):
        self.driver = driver

    def update_cv(self):
        print("Update CV Function")
        update_field = self.driver.find_element(By.XPATH, "//button[normalize-space()='Update your CV']")
        update_field.click()

    def upload_valid_cv(self):
        print("Upload Valid CV Function")
        file_input = self.driver.find_element(By.CSS_SELECTOR, "[data-testid='upload-cv-input']")
        file_path = os.path.join(os.getcwd(), "fixtures" , "larcilla_resume.docx")
        print(f"Uploading Valid File: {file_path}")
        file_input.send_keys(file_path)

    def upload_invalid_cv(self):
        print("Upload Invalid CV Function ")
        upload_field = self.driver.find_element(By.XPATH, "//button[@data-testid='upload-cv-button']")
        upload_field.click()
        file_input = self.driver.find_element(By.CSS_SELECTOR, "[data-testid='upload-cv-input']")
        file_path = os.path.join(os.getcwd(), "fixtures", "invalid_cv_file_type.pptx")
        print(f"Uploading Invalid File: {file_path}")
        file_input.send_keys(file_path)

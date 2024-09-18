from selenium.webdriver.common.by import By

class ExperienceSkillsPage:
    def __init__(self, driver):
        self.driver = driver

    def get_new_job_details(self):
        new_job_details = self.driver.find_element(By.XPATH, "//fieldset[@class='sc-jqCOkK crmKNd']")
        return new_job_details

    def get_pre_filled_data(self):
        experience_and_skills_field = self.driver.find_elements(By.XPATH,
            "//div[@class='Content-sc-191qdj-0 eDTANW']//ul[@class='sc-gzOgki ilqnAy']//li[@class='sc-kTUwUJ iVVMVF']")
        return experience_and_skills_field
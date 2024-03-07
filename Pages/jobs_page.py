import time

from selenium.webdriver import Keys, ActionChains

from Locators.jobs_page_locs import JobsPageLocators
from Pages.base_page import BasePage


class JobsPage(BasePage):

    def __init__(self) -> None:
        pass

    def check_url_of_jobs_page(self):
        jobs_url = "url removed"
        self.driver.current_url == jobs_url, f"Expected {jobs_url}, insead of {self.driver.current_url}"

    def check_presence_of_delivery_job(self):
        self.driver.find_element(*JobsPageLocators.delivery_job_section).click()
        assert self.driver.find_element(*JobsPageLocators.delivery_job_section).is_displayed(), "Job not displayed"

    def check_presence_of_cooking_job(self):
        self.driver.find_element(*JobsPageLocators.cooking_job_section).click()
        assert self.driver.find_element(*JobsPageLocators.cooking_job_section).is_displayed(), "Job not displayed"

    def check_presence_of_shift_manager_job(self):
        self.driver.find_element(*JobsPageLocators.shift_manager_section).click()
        assert self.driver.find_element(*JobsPageLocators.shift_manager_section).is_displayed(), "Job not displayed"

    def check_presence_of_unit_manager_job(self):
        self.driver.find_element(*JobsPageLocators.unit_manager_section).click()
        assert self.driver.find_element(*JobsPageLocators.unit_manager_section).is_displayed(), "Job not displayed"

    def check_presence_of_calls_operator_job(self):
        self.driver.find_element(*JobsPageLocators.calls_operator_section).click()
        assert self.driver.find_element(*JobsPageLocators.calls_operator_section).is_displayed(), "Job not displayed"

    def check_informations_displayed_about_delivery_job(self):
        self.driver.find_element(*JobsPageLocators.delivery_job_section).click()
        time.sleep(0.3)
        assert self.driver.find_element(
            *JobsPageLocators.delivery_informations_box).is_displayed(), "Informations not present"

    def check_informations_displayed_about_cooking_job(self):
        self.driver.find_element(*JobsPageLocators.cooking_job_section).click()
        time.sleep(0.3)
        assert self.driver.find_element(
            *JobsPageLocators.cooking_informations_box).is_displayed(), "Informations not present"

    def check_informations_displayed_about_shift_manager_job(self):
        self.driver.find_element(*JobsPageLocators.shift_manager_section).click()
        time.sleep(0.3)
        assert self.driver.find_element(
            *JobsPageLocators.shift_manager_informations_box).is_displayed(), "Informations not present"

    def check_informations_displayed_about_unit_manager_job(self):
        self.driver.find_element(*JobsPageLocators.unit_manager_section).click()
        time.sleep(0.3)
        assert self.driver.find_element(
            *JobsPageLocators.unit_manager_informations_box).is_displayed(), "Informations not present"

    def check_informations_displayed_about_calls_operator_job(self):
        self.driver.find_element(*JobsPageLocators.calls_operator_section).click()
        time.sleep(0.3)
        assert self.driver.find_element(
            *JobsPageLocators.calls_operator_informations_box).is_displayed(), "Informations not present"

    def send_inputs_for_job_apply(self):
        self.driver.find_element(*JobsPageLocators.name_input).click()
        self.driver.find_element(*JobsPageLocators.name_input).send_keys("Testing Apply")
        self.driver.find_element(*JobsPageLocators.phone_number_input).click()
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.NUMPAD0).perform()
        actions.send_keys(Keys.NUMPAD7).perform()
        actions.send_keys(Keys.NUMPAD7).perform()
        actions.send_keys(Keys.NUMPAD8).perform()
        actions.send_keys(Keys.NUMPAD1).perform()
        actions.send_keys(Keys.NUMPAD2).perform()
        actions.send_keys(Keys.NUMPAD3).perform()
        actions.send_keys(Keys.NUMPAD4).perform()
        actions.send_keys(Keys.NUMPAD5).perform()
        actions.send_keys(Keys.NUMPAD6).perform()
        # time.sleep(1)
        self.driver.find_element(*JobsPageLocators.mail_input).click()
        time.sleep(0.1)
        self.driver.find_element(*JobsPageLocators.mail_input).send_keys("TestingProjectMail@gmail.com")

    def select_city_Bucharest(self):
        for i in range(2):
            try:
                self.driver.find_element(*JobsPageLocators.select_city_Bucharest_input).click()
            except:
                pass
        for i in range(2):
            try:
                self.driver.find_element(*JobsPageLocators.select_Sector6_Bucharest_input).click()
            except:
                pass

    def agree_with_terms_and_conditions(self):
        for i in range(2):
            try:
                self.driver.find_element(*JobsPageLocators.agree_with_terms_input).click()
            except:
                pass

    def apply_for_delivery_job_with_company_car(self):
        self.driver.find_element(*JobsPageLocators.delivery_btn_input).click()
        time.sleep(0.1)
        for i in range(2):
            try:
                self.driver.find_element(*JobsPageLocators.delivery_with_company_car_btn_input).click()
            except:
                pass
        self.select_city_Bucharest()
        self.agree_with_terms_and_conditions()

    def apply_for_delivery_job_with_personal_car(self):
        self.driver.find_element(*JobsPageLocators.delivery_btn_input).click()
        time.sleep(0.2)
        for i in range(6):
            try:
                self.driver.find_element(*JobsPageLocators.delivery_with_personal_car_btn_input).click()
            except:
                pass
        time.sleep(0.2)
        self.select_city_Bucharest()
        self.agree_with_terms_and_conditions()

    def apply_for_cooking_job(self):
        self.driver.find_element(*JobsPageLocators.cooking_btn_input).click()
        time.sleep(0.1)
        self.select_city_Bucharest()
        self.agree_with_terms_and_conditions()

    def apply_for_shift_manager_job(self):
        self.driver.find_element(*JobsPageLocators.shift_manager_input).click()
        time.sleep(0.1)
        self.agree_with_terms_and_conditions()

    def apply_for_unit_manager_job(self):
        self.driver.find_element(*JobsPageLocators.unit_manager_input).click()
        time.sleep(0.1)
        self.agree_with_terms_and_conditions()

    def apply_for_calls_operator_job(self):
        self.driver.find_element(*JobsPageLocators.calls_operator_input).click()
        time.sleep(0.1)
        self.agree_with_terms_and_conditions()

    def send_the_application_further(self):
        self.driver.find_element(*JobsPageLocators.send_application_btn).click()

    def check_confirmation_text_message_after_application(self):
        assert self.driver.find_element(
            *JobsPageLocators.confirmation_message_box) != "", "Message is not as expected"

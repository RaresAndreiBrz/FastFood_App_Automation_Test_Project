import time

from selenium.webdriver import ActionChains

from Locators.cart_page_locs import CartPageLocators
from Locators.homepage_locs import HomepageLocators
from Pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys


class Homepage(BasePage):

    def __init__(self) -> None:
        pass

    def accept_cookies(self):
        time.sleep(0.5)
        self.driver.find_element(*HomepageLocators.accept_cookie_btn).click()
        time.sleep(0.5)

    def get_logo(self):
        logo = self.driver.find_element(*HomepageLocators.logo).is_displayed()
        return logo

    def click_on_location_btn(self):
        self.driver.find_element(*HomepageLocators.location_btn).click()

    def select_city(self):
        for i in range(100):
            try:
                self.driver.find_element(*HomepageLocators.city_btn).click()
                action = ActionChains(self.driver)
                for x in range(3):
                    action.send_keys(Keys.ARROW_DOWN).perform()
                action.send_keys(Keys.ENTER).perform()
                break
            except:
                pass

    def select_town(self):
        for i in range(10):
            try:
                self.driver.find_element(*HomepageLocators.town_btn).click()
                action = ActionChains(self.driver)
                action.send_keys(Keys.ARROW_DOWN).perform()
                action.send_keys(Keys.ENTER).perform()
                self.driver.find_element(*HomepageLocators.select_btn).click()
                break
            except:
                pass

    def select_location_auto(self):
        self.select_city()
        self.select_town()

    def setup_intro_cookies_and_location(self):
        self.accept_cookies()
        self.select_location_auto()
        time.sleep(0.5)

    def click_on_My_Account(self):
        self.driver.find_element(*HomepageLocators.my_account_btn).click()
        time.sleep(0.2)

    def click_on_first_enter_account_btn(self):
        self.driver.find_element(*HomepageLocators.enter_acc_btn1).click()

    def click_on_second_enter_account_btn(self):
        self.driver.find_element(*HomepageLocators.enter_acc_btn2).click()
        time.sleep(1)

    def click_on_create_account(self):
        self.driver.find_element(*HomepageLocators.create_acc_btn).click()
        time.sleep(0.5)

    def send_correct_mail_input(self):
        self.driver.find_element(*HomepageLocators.input_saved_mail).click()
        self.driver.find_element(*HomepageLocators.input_saved_mail).send_keys("VALID MAIL INPUT")

    def send_invalid_mail_input(self, invalid_mail):
        self.driver.find_element(*HomepageLocators.input_saved_mail).click()
        self.driver.find_element(*HomepageLocators.input_saved_mail).send_keys(f"{invalid_mail}")

    def send_mail_input_for_registration(self, invalid_mail):
        self.driver.find_element(*HomepageLocators.input_mail).click()
        self.driver.find_element(*HomepageLocators.input_mail).send_keys(f"{invalid_mail}")

    def send_correct_pwd_input(self):
        self.driver.find_element(*HomepageLocators.input_saved_pwd).click()
        self.driver.find_element(*HomepageLocators.input_saved_pwd).send_keys("VALID PWD INPUT")

    def send_invalid_pwd_input(self, invalid_pwd):
        self.driver.find_element(*HomepageLocators.input_saved_pwd).click()
        self.driver.find_element(*HomepageLocators.input_saved_pwd).send_keys(f"{invalid_pwd}")

    def click_on_About_btn(self):
        self.driver.find_element(*HomepageLocators.about_btn).click()
        time.sleep(0.3)
    def click_on_Magazine_btn(self):
        self.driver.find_element(*HomepageLocators.shops_btn).click()


    def click_on_Menu_dropdown_btn(self):
        self.driver.find_element(*HomepageLocators.menu_main_btn).click()
        time.sleep(1)

    def click_on_loyalty_section(self):
        self.driver.find_element(*HomepageLocators.loyalty_policy_btn).click()
        time.sleep(1)

    def click_on_offers_btn(self):
        self.driver.find_element(*HomepageLocators.offers_btn).click()
        time.sleep(0.2)

    def go_to_Terms_Conditions(self):
        self.driver.find_element(*HomepageLocators.terms_conditions_btn).click()
        time.sleep(0.2)

    def go_to_Policy_of_Confidentiality(self):
        self.driver.find_element(*HomepageLocators.confidentiality_policy_btn).click()
        time.sleep(0.2)

    def go_to_jobs_section(self):
        self.click_on_About_btn()
        self.driver.find_element(*HomepageLocators.about_jobs_dropdown_btn).click()
        time.sleep(0.2)


    def go_to_contact_section(self):
        self.click_on_About_btn()
        self.driver.find_element(*HomepageLocators.about_contact_dropdown_btn).click()
        time.sleep(0.2)

    def go_to_night_schedule_page(self):
        self.driver.find_element(*HomepageLocators.night_schedule_program_btn).click()
        time.sleep(0.2)

    def check_night_schedule_informations(self):
        box_info = self.driver.find_element(*HomepageLocators.night_schedule_box_info).text
        print(box_info)
        text_to_check = "valoare mai mica de 60 lei livrate in intervalul de functionare in regim"
        assert text_to_check in box_info, "Expected text does not show up."

    def go_to_facebook_page(self):
        self.driver.find_element(*HomepageLocators.facebook_page_btn).click()
        time.sleep(0.2)


    def go_to_campaigns_section(self):
        self.click_on_About_btn()
        self.driver.find_element(*HomepageLocators.about_campaigns_dropdown_btn).click()
        time.sleep(0.2)

    def go_to_grams_section(self):
        self.click_on_About_btn()
        self.driver.find_element(*HomepageLocators.about_quantities_dropdown_btn).click()

    def go_to_news_section(self):
        self.click_on_About_btn()
        for i in range(10):
            try:
                self.driver.find_element(*HomepageLocators.about_news_dropdown_btn).click()
            except:
                pass
        time.sleep(3)

    def go_to_products_section(self):
        self.click_on_About_btn()
        time.sleep(1)
        self.driver.find_element(*HomepageLocators.about_products_dropdown_btn).click()
        time.sleep(0.2)

    def select_calzone_from_menu_list(self):
        self.driver.find_element(*HomepageLocators.calzone_dropdown_btn).click()

    def select_calzone_from_homepage_directly(self):
        max_attempts = 5
        for _ in range(max_attempts):
            try:
                self.driver.find_element(*HomepageLocators.calzone_homepg_btn).click()
                break
            except:
                time.sleep(0.5)

    def go_to_calzone_from_menu_dropdown_list(self):
        self.click_on_Menu_dropdown_btn()
        self.select_calzone_from_menu_list()

    def go_to_salads_from_menu_dropdown_list(self):
        self.click_on_Menu_dropdown_btn()
        self.driver.find_element(*HomepageLocators.salads_dropdown_btn).click()
        time.sleep(0.5)

    def go_to_desert_from_menu_dropdown_list(self):
        self.click_on_Menu_dropdown_btn()
        time.sleep(0.1)
        self.driver.find_element(*HomepageLocators.deserts_dropdown_btn).click()
        time.sleep(0.3)

    def go_to_drinks_from_menu_dropdown_list(self):
        self.click_on_Menu_dropdown_btn()
        self.driver.find_element(*HomepageLocators.drinks_dropdown_btn).click()
        time.sleep(0.3)

    def go_to_sausage_from_menu_dropdown_list(self):
        self.click_on_Menu_dropdown_btn()
        self.driver.find_element(*HomepageLocators.sausage_dropdown_btn).click()
        time.sleep(0.3)

    def send_first_name_input(self, first_name):
        name = self.driver.find_elements(*HomepageLocators.input_name)
        name1 = name[0]
        name1.send_keys(f"{first_name}")

    def send_last_name_input(self, last_name):
        name = self.driver.find_elements(*HomepageLocators.input_name)
        name2 = name[1]
        name2.send_keys(f"{last_name}")

    def send_phone_number_for_registration(self, nine_digits_nr):
        self.driver.find_element(*HomepageLocators.input_phone_number).click()
        self.driver.find_element(*HomepageLocators.input_phone_number).send_keys(f"{nine_digits_nr}")

    def send_password_for_registration(self, pwd_input):
        pwds = self.driver.find_elements(*HomepageLocators.pwd_inputs)
        first_pwd = pwds[0]
        first_pwd.send_keys(f"{pwd_input}")

    def send_password_confirmation_ssfor_registration(self, pwd_input):
        pwds = self.driver.find_elements(*HomepageLocators.pwd_inputs)
        sec_pwd = pwds[1]
        sec_pwd.send_keys(f"{pwd_input}")

    def finish_creating_account_process(self):
        self.driver.find_element(*HomepageLocators.terms_conditions_btn).click()
        for i in range(11):
            try:
                self.driver.find_element(*HomepageLocators.create_acc_final_btn).click()
            except:
                pass
        try:
            self.driver.find_element(*HomepageLocators.no_offers_to_receive_button_pop_up).click()
            self.driver.find_element(*HomepageLocators.create_acc_final_btn).click()
        except:
            pass

    def check_confirmation_sms_popUp_shows_up(self):
        sms_pop_up = self.driver.wait_for_element(*HomepageLocators.confirmation_sms_pop_up)
        assert sms_pop_up.is_displayed(), "PopUP SMS did not appear"

    def log_in(self):
        self.click_on_My_Account()
        self.click_on_first_enter_account_btn()
        self.send_correct_mail_input()
        self.send_correct_pwd_input()
        self.click_on_second_enter_account_btn()
        time.sleep(3)

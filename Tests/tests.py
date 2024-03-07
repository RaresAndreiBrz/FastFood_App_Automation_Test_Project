import time

from selenium.webdriver import Keys, ActionChains

from Locators.drinks_page_locs import DrinksPageLocators
from Locators.homepage_locs import HomepageLocators
from Tests.base_test import BaseTests


class Tests(BaseTests):


#GENERAL BUTTONS AND HOMEPAGE
    def test_load_homepage_in_reasonable_time(self):
        start_time = time.time()
        self.driver.get("APP ADDRESS NOT GIVEN")
        self.driver.implicitly_wait(10)
        end_time = time.time()
        load_time = end_time - start_time
        reasonable_load_time = 5.0
        assert load_time < reasonable_load_time, f"Page load time ({load_time}s) exceeds the threshold."

    def test_logo_shown_on_homepage(self):
        self.homepage_object.setup_intro_cookies_and_location()
        element = self.homepage_object.get_logo()
        assert bool(element) == True, "Logo not displayed on page"


    def test_actions_back_and_forward(self):
        self.homepage_object.setup_intro_cookies_and_location()
        self.homepage_object.select_calzone_from_homepage_directly()
        self.driver.back()
        self.wait_for_displayed_element(HomepageLocators.logo)
        self.driver.forward()
        self.wait_for_displayed_element(HomepageLocators.logo)
        assert self.driver.current_url == "url removed for this test", "Current URL doesn't match expected URL."


    def test_menu_buttons_are_displayed(self):
        self.homepage_object.setup_intro_cookies_and_location()
        assert self.driver.find_element(*HomepageLocators.menu_main_btn).is_displayed(), "Not all buttons are displayed, all expected to be displayed."
        assert self.driver.find_element(*HomepageLocators.about_btn).is_displayed(), "Not all buttons are displayed, all expected to be displayed."
        assert self.driver.find_element(*HomepageLocators.shops_btn).is_displayed(), "Not all buttons are displayed, all expected to be displayed."
        assert self.driver.find_element(*HomepageLocators.home_btn).is_displayed(), "Not all buttons are displayed, all expected to be displayed."
        assert self.driver.find_element(*HomepageLocators.offers_btn).is_displayed(), "Not all buttons are displayed, all expected to be displayed."


    def test_menu_dropdown_list_is_displayed_after_click_on_it(self):
        self.homepage_object.setup_intro_cookies_and_location()
        self.homepage_object.click_on_Menu_dropdown_btn()
        time.sleep(1)
        assert self.driver.find_element(*HomepageLocators.budget_dropdown_btn).is_displayed(), "Budget button is not displayed"
        assert self.driver.find_element(*HomepageLocators.offers_dropdown_btn).is_displayed(), "Offers button is not displayed"
        assert self.driver.find_element(*HomepageLocators.loyalty_dropdown_btn).is_displayed(), "Loyalty button is not displayed"
        assert self.driver.find_element(*HomepageLocators.pizza_dropdown_btn).is_displayed(), "Pizza button is not displayed"
        assert self.driver.find_element(*HomepageLocators.stripwich_dropdown_btn).is_displayed(), "Stripwich button is not displayed"
        assert self.driver.find_element(*HomepageLocators.calzone_dropdown_btn).is_displayed(), "Calzone button is not displayed"
        assert self.driver.find_element(*HomepageLocators.chicken_dropdown_btn).is_displayed(), "Chicken button is not displayed"
        assert self.driver.find_element(*HomepageLocators.sides_dropdown_btn).is_displayed(), "Sides button is not displayed"
        assert self.driver.find_element(*HomepageLocators.salads_dropdown_btn).is_displayed(), "Salads button is not displayed"
        assert self.driver.find_element(*HomepageLocators.pasta_dropdown_btn).is_displayed(), "Pasta button is not displayed"
        assert self.driver.find_element(*HomepageLocators.deserts_dropdown_btn).is_displayed(), "Deserts button is not displayed"
        assert self.driver.find_element(*HomepageLocators.drinks_dropdown_btn).is_displayed(), "Drinks button is not displayed"
        assert self.driver.find_element(*HomepageLocators.sausage_dropdown_btn).is_displayed(), "Sausage button is not displayed"
        assert self.driver.find_element(*HomepageLocators.menus_dropdown_btn).is_displayed(), "Menus button is not displayed"



    def test_calzone_button_directly_from_homepage(self):
        self.homepage_object.setup_intro_cookies_and_location()
        time.sleep(1)
        for i in range(4):
            try:
                self.driver.find_element(*HomepageLocators.calzone_homepg_btn).click()
            except:
                pass
        time.sleep(1)
        expected_url1 = "url removed for this test"
        assert self.driver.current_url == expected_url1, f"Expected 'Calzone' page instead of '{self.driver.current_url}'"


    def test_salads_button_directly_from_homepage(self):
        self.homepage_object.setup_intro_cookies_and_location()
        time.sleep(1)
        for i in range(4):
            try:
                self.driver.find_element(*HomepageLocators.salads_homepg_btn).click()
            except:
                pass
        time.sleep(1)
        expected_url1 = "url removed for this test"
        assert self.driver.current_url == expected_url1, f"Expected 'Salads' page instead of '{self.driver.current_url}'"


    def test_desert_button_directly_from_homepage(self):
        self.homepage_object.setup_intro_cookies_and_location()
        time.sleep(1)
        for i in range(4):
            try:
                self.driver.find_element(*HomepageLocators.desert_homepg_btn).click()
            except:
                pass
        time.sleep(1)
        expected_url1 = "url removed for this test"
        assert self.driver.current_url == expected_url1, f"Expected 'Deserts' page instead of '{self.driver.current_url}'"


    def test_drinks_button_directly_from_homepage(self):
        self.homepage_object.setup_intro_cookies_and_location()
        time.sleep(1)
        for i in range(4):
            try:
                self.driver.find_element(*HomepageLocators.drinks_homepg_btn).click()
            except:
                pass
        time.sleep(1)
        expected_url1 = "url removed for this test"
        assert self.driver.current_url == expected_url1, f"Expected 'Drinks' page instead of '{self.driver.current_url}'"


    def test_sausages_button_directly_from_homepage(self):
        self.homepage_object.setup_intro_cookies_and_location()
        time.sleep(1)
        for i in range(4):
            try:
                self.driver.find_element(*HomepageLocators.sausages_homepg_btn).click()
            except:
                pass
        time.sleep(1)
        expected_url1 = "url removed for this test"
        assert self.driver.current_url == expected_url1, f"Expected 'Sausages' page instead of '{self.driver.current_url}'"


        # TEST FAILS. 'FAVORITE' BUTTON DOES NOT SHOW UP, AT LEAST NOT IN AUTOMATED TESTS. MANUALLY, THEY DO.
    def test_add_to_favorite_button_is_displayed(self):
        self.homepage_object.setup_intro_cookies_and_location()
        self.homepage_object.go_to_drinks_from_menu_dropdown_list()
        time.sleep(1)
        assert self.driver.find_element(*DrinksPageLocators.add_favorite_btn).is_displayed(), "'Favorite' button is not displayed."


    def test_link_towards_terms_and_conditions(self):
        self.homepage_object.setup_intro_cookies_and_location()
        time.sleep(2)
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.SPACE * 3).perform()
        time.sleep(1)
        self.homepage_object.go_to_Terms_Conditions()
        time.sleep(1)
        url_needed = "url removed for this test"
        assert self.driver.current_url == url_needed, f"Expected {url_needed} and received {self.driver.current_url}"

    def test_link_towards_Policy_of_Confidentiality(self):
        self.homepage_object.setup_intro_cookies_and_location()
        time.sleep(2)
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.SPACE * 3).perform()
        time.sleep(1)
        self.homepage_object.go_to_Policy_of_Confidentiality()
        url_needed = "url removed for this test"
        assert self.driver.current_url == url_needed, f"Expected {url_needed} and received {self.driver.current_url}"

    def test_button_towards_shops_locations(self):
        self.homepage_object.setup_intro_cookies_and_location()
        self.homepage_object.click_on_Magazine_btn()
        time.sleep(1)
        url_needed = "url removed for this test"
        assert self.driver.current_url == url_needed, f"Expected {url_needed} and received {self.driver.current_url}"

    def test_button_towards_Special_Offers(self):
        self.homepage_object.setup_intro_cookies_and_location()
        self.homepage_object.click_on_offers_btn()
        url_needed = "url removed for this test"
        assert self.driver.current_url == url_needed, f"Expected {url_needed} and received {self.driver.current_url}"

    def test_button_towards_Contact_section(self):
        self.homepage_object.setup_intro_cookies_and_location()
        self.homepage_object.go_to_contact_section()
        url_needed = "url removed for this test"
        assert self.driver.current_url == url_needed, f"Expected {url_needed} and received {self.driver.current_url}"

    def test_button_towards_Campaign_section(self):
        self.homepage_object.setup_intro_cookies_and_location()
        self.homepage_object.go_to_campaigns_section()
        url_needed = "url removed for this test"
        assert self.driver.current_url == url_needed, f"Expected {url_needed} and received {self.driver.current_url}"

    def test_button_towards_Loyalty_section(self):
        self.homepage_object.setup_intro_cookies_and_location()
        time.sleep(2)
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.SPACE * 3).perform()
        time.sleep(1)
        self.homepage_object.click_on_loyalty_section()
        url_needed = "url removed for this test"
        assert self.driver.current_url == url_needed, f"Expected {url_needed} and received {self.driver.current_url}"


        #BUTTON FROM 'ABOUT' DROPDOWN LIST DOES NOT WORK. AN INFORMATION PAGE OR PDF FILE SHOULD POP UP
    def test_button_towards_Grams_and_allergies_section_from_dropdown_About_btn(self):
        self.homepage_object.setup_intro_cookies_and_location()
        self.homepage_object.go_to_grams_section()
        time.sleep(1)
        unexpected_url = "url removed for this test"
        time.sleep(4)
        assert self.driver.current_url != unexpected_url, f"Receiveded '{unexpected_url}' page instead of page regarding allergies"


    def test_schedule_night_hours_link_is_functional(self):
        self.homepage_object.setup_intro_cookies_and_location()
        time.sleep(2)
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.SPACE * 3).perform()
        time.sleep(1)
        self.homepage_object.go_to_night_schedule_page()
        time.sleep(3)
        night_url = "url removed for this test"
        assert self.driver.current_url == night_url, f"Receiveded '{self.driver.current_url}' page instead of page regarding night schedule"

    def test_schedule_night_page_displays_correct_informations(self):
        self.homepage_object.setup_intro_cookies_and_location()
        time.sleep(2)
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.SPACE * 3).perform()
        time.sleep(1)
        self.homepage_object.go_to_night_schedule_page()
        time.sleep(2)
        self.homepage_object.check_night_schedule_informations()

    def test_url_received_after_clicking_on_facebook_shortcut_button(self):
        self.homepage_object.setup_intro_cookies_and_location()
        time.sleep(2)
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.SPACE * 3).perform()
        time.sleep(1)
        self.homepage_object.go_to_facebook_page()
        time.sleep(1)
        facebook_url = "url removed for this test"
        assert self.driver.current_url == facebook_url, f"Receiveded '{self.driver.current_url}' page instead of {facebook_url}"



#JOBS PAGE TESTS

    def test_jobs_page_is_correctly_displayed(self):
        self.homepage_object.setup_intro_cookies_and_location()
        self.homepage_object.go_to_jobs_section()
        expected_url = "url removed for this test"
        assert self.driver.current_url == expected_url, f"Expected '{expected_url}' page instead of '{self.driver.current_url}'"

    def test_jobs_are_available(self):
        self.homepage_object.setup_intro_cookies_and_location()
        self.homepage_object.go_to_jobs_section()
        self.jobspage_object.check_presence_of_delivery_job()
        self.jobspage_object.check_presence_of_cooking_job()
        self.jobspage_object.check_presence_of_shift_manager_job()
        self.jobspage_object.check_presence_of_unit_manager_job()
        self.jobspage_object.check_presence_of_calls_operator_job()

    def test_jobs_descriptions_are_available(self):
        self.homepage_object.setup_intro_cookies_and_location()
        self.homepage_object.go_to_jobs_section()
        self.jobspage_object.check_informations_displayed_about_delivery_job()
        self.jobspage_object.check_informations_displayed_about_cooking_job()
        self.jobspage_object.check_informations_displayed_about_shift_manager_job()
        self.jobspage_object.check_informations_displayed_about_unit_manager_job()
        self.jobspage_object.check_informations_displayed_about_calls_operator_job()

    def test_applying_for_delivery_job_using_personal_car_without_CV(self):
        self.homepage_object.setup_intro_cookies_and_location()
        self.homepage_object.go_to_jobs_section()
        self.jobspage_object.send_inputs_for_job_apply()
        self.jobspage_object.apply_for_delivery_job_with_personal_car()
        time.sleep(1)
        # self.jobspage_object.send_the_application_further() ------------ Activating this line and running the test, it will create an applying. Also, the line below confirms the test till last step.
        self.jobspage_object.check_url_of_jobs_page()

    def test_applying_for_delivery_job_using_company_car_without_CV(self):
        self.homepage_object.setup_intro_cookies_and_location()
        self.homepage_object.go_to_jobs_section()
        self.jobspage_object.send_inputs_for_job_apply()
        self.jobspage_object.apply_for_delivery_job_with_company_car()
        time.sleep(1)
        # self.jobspage_object.send_the_application_further() ------------ Activating this line and running the test, it will create an applying. Also, the line below confirms the test till last step.
        self.jobspage_object.check_url_of_jobs_page()

    def test_applying_for_cooking_job_without_CV(self):
        self.homepage_object.setup_intro_cookies_and_location()
        self.homepage_object.go_to_jobs_section()
        self.jobspage_object.send_inputs_for_job_apply()
        self.jobspage_object.apply_for_cooking_job()
        time.sleep(1)
        # self.jobspage_object.send_the_application_further() ------------ Activating this line and running the test, it will create an applying. Also, the line below confirms the test till last step.
        self.jobspage_object.check_url_of_jobs_page()

    def test_applying_for_shift_manager_job_without_CV(self):
        self.homepage_object.setup_intro_cookies_and_location()
        self.homepage_object.go_to_jobs_section()
        self.jobspage_object.send_inputs_for_job_apply()
        self.jobspage_object.apply_for_shift_manager_job()
        time.sleep(1)
        # self.jobspage_object.send_the_application_further() ------------ Activating this line and running the test, it will create an applying. Also, the line below confirms the test till last step.
        self.jobspage_object.check_url_of_jobs_page()

    def test_applying_for_unit_manager_job_without_CV(self):
        self.homepage_object.setup_intro_cookies_and_location()
        self.homepage_object.go_to_jobs_section()
        self.jobspage_object.send_inputs_for_job_apply()
        self.jobspage_object.apply_for_unit_manager_job()
        time.sleep(1)
        # self.jobspage_object.send_the_application_further() ------------ Activating this line and running the test, it will create an applying. Also, the line below confirms the test till last step.
        self.jobspage_object.check_url_of_jobs_page()

    def test_applying_for_calls_operator_job_without_CV(self):
        self.homepage_object.setup_intro_cookies_and_location()
        self.homepage_object.go_to_jobs_section()
        self.jobspage_object.send_inputs_for_job_apply()
        self.jobspage_object.apply_for_calls_operator_job()
        time.sleep(1)
        # self.jobspage_object.send_the_application_further() ------------ Activating this line and running the test, it will create an applying. Also, the line below confirms the test till last step.
        self.jobspage_object.check_url_of_jobs_page()


#NEWS PAGE TESTS

    def test_news_page_is_correctly_displayed(self):
        self.homepage_object.setup_intro_cookies_and_location()
        self.homepage_object.go_to_news_section()
        self.newspage_object.check_presence_of_news_page()

    def test_last_story_is_displayed(self):

        self.homepage_object.setup_intro_cookies_and_location()
        self.homepage_object.go_to_news_section()
        time.sleep(5)
        self.newspage_object.check_presence_of_last_news_subject_Cluj()
    def test_multiple_stories_are_displayed(self):
        self.homepage_object.setup_intro_cookies_and_location()
        self.homepage_object.go_to_news_section()
        time.sleep(5)
        self.newspage_object.check_multiple_news_are_displayed()

    def test_short_story_info_displayed_on_news_page(self):
        self.homepage_object.setup_intro_cookies_and_location()
        self.homepage_object.go_to_news_section()
        time.sleep(5)
        self.newspage_object.check_introductions_of_news_texts_are_displayed()

    def test_images_displayed_on_stories(self):
        self.homepage_object.setup_intro_cookies_and_location()
        self.homepage_object.go_to_news_section()
        time.sleep(5)
        self.newspage_object.news_contains_multiple_images()

    def test_image_displayed_on_a_specific_story(self):
        self.homepage_object.setup_intro_cookies_and_location()
        self.homepage_object.go_to_news_section()
        time.sleep(5)
        self.newspage_object.news_contains_image()

    def test_story_date_in_page_and_in_details_both_coincide(self):
        self.homepage_object.setup_intro_cookies_and_location()
        self.homepage_object.go_to_news_section()
        time.sleep(3)
        self.newspage_object.check_time_corresponds_in_between_pages()

    def test_all_dates_are_different(self):
        self.homepage_object.setup_intro_cookies_and_location()
        self.homepage_object.go_to_news_section()
        time.sleep(7)
        self.newspage_object.check_date_of_story_displayed_only_once()

    def test_fifth_story_contains_displayed_informations(self):
        self.homepage_object.setup_intro_cookies_and_location()
        self.homepage_object.go_to_news_section()
        time.sleep(3)
        self.newspage_object.check_informations_of_fifth_story_are_displayed()

    def test_first_story_name_shows_up_correctly(self):
        self.homepage_object.setup_intro_cookies_and_location()
        self.homepage_object.go_to_news_section()
        time.sleep(2)
        self.newspage_object.check_name_of_the_first_story_is_correctly_displayed()

    def test_ninth_story_images_are_not_present(self):
        self.homepage_object.setup_intro_cookies_and_location()
        self.homepage_object.go_to_news_section()
        time.sleep(2)
        self.newspage_object.check_images_displayed_on_ninth_story()



#SALADS PAGE TESTS
    def test_more_than_three_products_are_displayed(self):
        self.homepage_object.setup_intro_cookies_and_location()
        self.homepage_object.go_to_salads_from_menu_dropdown_list()
        time.sleep(0.2)
        self.saladspage_object.check_presence_of_more_than_three_products_displayed_on_page()

    def test_presence_of_Tuna_and_Home_salads(self):
        self.homepage_object.setup_intro_cookies_and_location()
        self.homepage_object.go_to_salads_from_menu_dropdown_list()
        time.sleep(0.2)
        self.saladspage_object.check_Home_Salad_is_available()
        self.saladspage_object.check_Tuna_Salad_is_available()

    def test_presence_of_Caesar_and_Veggie_salads(self):
        self.homepage_object.setup_intro_cookies_and_location()
        self.homepage_object.go_to_salads_from_menu_dropdown_list()
        time.sleep(0.2)
        self.saladspage_object.check_Caesar_Salad_is_available()
        self.saladspage_object.check_Veggie_Salad_is_available()

    def test_description_available_on_each_product(self):
        self.homepage_object.setup_intro_cookies_and_location()
        self.homepage_object.go_to_salads_from_menu_dropdown_list()
        time.sleep(0.2)
        self.saladspage_object.check_short_intro_of_all_products()

    def test_informations_button_about_a_salad(self):
        self.homepage_object.setup_intro_cookies_and_location()
        self.homepage_object.go_to_salads_from_menu_dropdown_list()
        time.sleep(0.2)
        self.saladspage_object.check_informations_button_of_a_salad()




#ABOUT PRODUCTS PAGE TESTS
    def test_about_products_page_is_displayed(self):
        self.homepage_object.setup_intro_cookies_and_location()
        self.homepage_object.go_to_products_section()
        expected_url = "URL REMOVED"
        assert self.driver.current_url == expected_url, f'Expected "{expected_url}" instead of {self.driver.current_url}'

    def test_title_present_on_the_page(self):
        self.homepage_object.setup_intro_cookies_and_location()
        self.homepage_object.go_to_products_section()
        self.aboutprod_object.check_if_page_title_is_displayed()

    def test_product_pizza_is_present_on_the_page(self):
        self.homepage_object.setup_intro_cookies_and_location()
        self.homepage_object.go_to_products_section()
        self.aboutprod_object.check_if_product_pizza_is_displayed()

    def test_description_of_the_product_pizza_is_displayed(self):
        self.homepage_object.setup_intro_cookies_and_location()
        self.homepage_object.go_to_products_section()
        time.sleep(0.5)
        self.aboutprod_object.check_if_pizza_description_is_available()

    def test_product_calzone_is_present_on_the_page(self):
        self.homepage_object.setup_intro_cookies_and_location()
        self.homepage_object.go_to_products_section()
        time.sleep(0.5)
        self.aboutprod_object.check_if_product_calzonee_is_displayed()

    def test_description_of_the_product_calzone_is_displayed(self):
        self.homepage_object.setup_intro_cookies_and_location()
        self.homepage_object.go_to_products_section()
        time.sleep(0.5)
        self.aboutprod_object.check_if_calzone_description_is_available()

    def test_product_stripwich_is_present_on_the_page(self):
        self.homepage_object.setup_intro_cookies_and_location()
        self.homepage_object.go_to_products_section()
        time.sleep(0.5)
        self.aboutprod_object.check_if_product_stripwich_is_displayed()

    def test_description_of_the_product_stripwich_is_displayed(self):
        self.homepage_object.setup_intro_cookies_and_location()
        self.homepage_object.go_to_products_section()
        time.sleep(0.5)
        self.aboutprod_object.check_if_stripwich_description_is_available()

    def test_product_bbqWings_is_present_on_the_page(self):
        self.homepage_object.setup_intro_cookies_and_location()
        self.homepage_object.go_to_products_section()
        time.sleep(0.5)
        self.aboutprod_object.check_if_product_bbq_wings_is_displayed()

    def test_description_of_the_product_bbqWings_is_displayed(self):
        self.homepage_object.setup_intro_cookies_and_location()
        self.homepage_object.go_to_products_section()
        time.sleep(0.5)
        self.aboutprod_object.check_if_bbq_wings_description_is_available()

    def test_product_pasta_is_present_on_the_page(self):
        self.homepage_object.setup_intro_cookies_and_location()
        self.homepage_object.go_to_products_section()
        time.sleep(0.5)
        self.aboutprod_object.check_if_product_pasta_is_displayed()

    def test_description_of_the_product_pasta_is_displayed(self):
        self.homepage_object.setup_intro_cookies_and_location()
        self.homepage_object.go_to_products_section()
        time.sleep(0.5)
        self.aboutprod_object.check_if_pasta_description_is_available()


#LOGIN PROCESS TESTS
    def test_authentication_button_is_displayed(self):
        self.homepage_object.setup_intro_cookies_and_location()
        assert self.driver.find_element(*HomepageLocators.my_account_btn).is_displayed(), "My Account button is not displayed"

    def test_succesfully_login(self):
        self.homepage_object.setup_intro_cookies_and_location()
        self.homepage_object.click_on_My_Account()
        self.homepage_object.click_on_first_enter_account_btn()
        self.homepage_object.send_correct_mail_input()
        self.homepage_object.send_correct_pwd_input()
        self.homepage_object.click_on_second_enter_account_btn()
        time.sleep(1)
        assert self.driver.find_element(*HomepageLocators.success_logged_in_mssg).text == "Autentificare cu succes.", "Not displayed"


    def test_login_with_invalid_mail_and_valid_pwd(self):
        self.homepage_object.setup_intro_cookies_and_location()
        self.homepage_object.click_on_My_Account()
        self.homepage_object.click_on_first_enter_account_btn()
        self.homepage_object.send_invalid_mail_input("hamham@gmail")
        self.homepage_object.send_correct_pwd_input()
        self.homepage_object.click_on_second_enter_account_btn()
        assert self.driver.find_element(
            *HomepageLocators.invalid_mail_message).text == "Introduceti o adresa de email valida.", "Not displayed"


    def test_login_with_invalid_mail_and_invalid_pwd(self):
        self.homepage_object.setup_intro_cookies_and_location()
        self.homepage_object.click_on_My_Account()
        self.homepage_object.click_on_first_enter_account_btn()
        self.homepage_object.send_invalid_mail_input("hamham@gmail")
        self.homepage_object.send_invalid_pwd_input("PASWD123.")
        self.homepage_object.click_on_second_enter_account_btn()
        assert self.driver.find_element(
            *HomepageLocators.invalid_mail_message).text == "Introduceti o adresa de email valida.", "Not displayed"

    def test_login_with_valid_mail_and_invalid_pwd(self):
        self.homepage_object.setup_intro_cookies_and_location()
        self.homepage_object.click_on_My_Account()
        self.homepage_object.click_on_first_enter_account_btn()
        self.homepage_object.send_correct_mail_input()
        self.homepage_object.send_invalid_pwd_input("biscuiti")
        self.homepage_object.click_on_second_enter_account_btn()
        assert self.wait_for_displayed_element(HomepageLocators.invalid_pwd_or_mail_message).text == "Parola este incorecta", "Not displayed"


    def test_login_witout_mail_and_invalid_pwd(self):
        self.homepage_object.setup_intro_cookies_and_location()
        self.homepage_object.click_on_My_Account()
        self.homepage_object.click_on_first_enter_account_btn()
        self.homepage_object.send_invalid_mail_input("")
        self.homepage_object.send_invalid_pwd_input("littleDogs")
        self.homepage_object.click_on_second_enter_account_btn()
        assert self.wait_for_displayed_element(HomepageLocators.invalid_mail_message).text == "Introduceti o adresa de email valida.", "Not displayed"

    def test_new_url_for_registering_an_account(self):
        self.homepage_object.setup_intro_cookies_and_location()
        self.homepage_object.click_on_My_Account()
        self.homepage_object.click_on_create_account()
        time.sleep(0.2)
        expected_url = "URL REMOVED"
        assert self.driver.current_url == expected_url, f"Expected {expected_url} and received {self.driver.current_url}"


# NOT PRESSING FINAL 'CREATE ACCOUNT' BUTTON IN AUTOMATION TEST
    def test_create_new_account_successfully(self):
        self.homepage_object.setup_intro_cookies_and_location()
        self.homepage_object.click_on_My_Account()
        self.homepage_object.click_on_create_account()
        self.homepage_object.send_first_name_input("Testing")
        self.homepage_object.send_last_name_input("Second name")
        self.homepage_object.send_mail_input_for_registration("testing.project@gmail.com")
        self.homepage_object.send_phone_number_for_registration("123456789")
        self.homepage_object.send_password_for_registration("sIMPLEpASSWORD")
        self.homepage_object.send_password_confirmation_ssfor_registration("sIMPLEpASSWORD")
        self.homepage_object.finish_creating_account_process()
        self.homepage_object.check_confirmation_sms_popUp_shows_up()



#CART AND ORDERS TESTS

    def test_prices_of_one_product_is_correctly_displayed_in_cart(self):
        self.homepage_object.setup_intro_cookies_and_location()
        self.homepage_object.log_in()
        self.homepage_object.go_to_drinks_from_menu_dropdown_list()
        self.drinkpage_object.select_fanta_option()
        take_price_of_product = self.drinkpage_object.total_price_text()
        self.itempage_object.add_the_product_to_cart()
        self.cartpage_object.click_on_cart_btn()
        total_price = self.cartpage_object.price_of_all_products()
        assert take_price_of_product == total_price, "Prices do not correspond"

    def test_invalid_promotion_code_inserted(self):
        self.homepage_object.setup_intro_cookies_and_location()
        self.homepage_object.log_in()
        self.homepage_object.go_to_sausage_from_menu_dropdown_list()
        time.sleep(2)
        self.homepage_object.click_on_My_Account()
        self.sausagespage_object.select_bbq_ss()
        time.sleep(2)
        self.itempage_object.select_ss_hot_bbq()
        self.itempage_object.add_the_product_to_cart()
        time.sleep(2)
        self.cartpage_object.go_to_checkout_page()
        time.sleep(1)
        self.checkoutpage_object.add_invalid_promotional_code_and_check_result("HeheCodeInvalid")

    def test_adding_one_calzone_product_cart_update(self):
        self.homepage_object.setup_intro_cookies_and_location()
        self.homepage_object.go_to_calzone_from_menu_dropdown_list()
        self.calzonepage_object.select_calzone_option()
        time.sleep(1)
        self.itempage_object.select_ss_sweet_bbq()
        self.itempage_object.select_three_random_toppings_for_calzone(3)
        self.itempage_object.select_better_baked()
        self.itempage_object.add_the_product_to_cart()
        self.cartpage_object.check_number_of_products_in_cart(1)

    def test_adding_multiple_calzone_products_cart_update(self):
        self.homepage_object.setup_intro_cookies_and_location()
        self.homepage_object.go_to_calzone_from_menu_dropdown_list()
        self.calzonepage_object.select_calzone_option()
        time.sleep(1)
        self.itempage_object.select_ss_sweet_bbq()
        self.itempage_object.select_three_random_toppings_for_calzone(3)
        self.itempage_object.select_better_baked()
        self.itempage_object.add_the_product_to_cart()
        self.calzonepage_object.select_menu_calzone_option()
        time.sleep(1)
        self.itempage_object.select_ss_sweet_bbq()
        self.itempage_object.select_three_random_toppings_for_calzone(3)
        self.itempage_object.select_extra_sos_bbq_sweet()
        self.itempage_object.select_freeDrink_water()
        self.itempage_object.add_the_product_to_cart()
        self.cartpage_object.check_number_of_products_in_cart(2)


    def test_price_from_product_page_is_equal_with_cart_price(self):
        self.homepage_object.setup_intro_cookies_and_location()
        self.homepage_object.log_in()
        self.homepage_object.go_to_calzone_from_menu_dropdown_list()
        time.sleep(1)
        first_price = self.calzonepage_object.take_price_of_calzone_displayed_on_page()
        self.calzonepage_object.select_calzone_option()
        self.itempage_object.fully_add_calzone_details_to_pruchase()
        self.cartpage_object.click_on_cart_btn()
        second_price = self.cartpage_object.take_price_of_calzone_displayed_on_cart()
        assert first_price == second_price, "Prices are different, as not as expected"

    def test_more_than_one_product_displayed_on_page(self):
        self.homepage_object.setup_intro_cookies_and_location()
        self.homepage_object.log_in()
        self.homepage_object.go_to_calzone_from_menu_dropdown_list()
        time.sleep(1)
        self.calzonepage_object.check_more_than_one_product_is_displayed_on_page()

    def test_getting_to_checkout_page(self):
        self.homepage_object.setup_intro_cookies_and_location()
        self.homepage_object.log_in()
        self.homepage_object.go_to_calzone_from_menu_dropdown_list()
        time.sleep(1)
        self.calzonepage_object.select_calzone_option()
        self.itempage_object.fully_add_calzone_details_to_pruchase()
        self.cartpage_object.go_to_checkout_page()
        self.checkoutpage_object.check_presence_of_checkout_page()

    def test_finish_an_order_process(self):
        self.homepage_object.setup_intro_cookies_and_location()
        self.homepage_object.log_in()
        self.homepage_object.go_to_drinks_from_menu_dropdown_list()
        time.sleep(0.5)
        self.drinkpage_object.select_redbull_option()
        time.sleep(0.5)
        self.itempage_object.add_the_product_to_cart()
        time.sleep(0.2)
        self.homepage_object.go_to_desert_from_menu_dropdown_list()
        time.sleep(0.2)
        self.desertpage_object.select_cherry_desert()
        time.sleep(0.3)
        self.itempage_object.add_the_product_to_cart()
        time.sleep(0.3)
        self.desertpage_object.select_brownie_desert()
        time.sleep(0.5)
        self.itempage_object.add_the_product_to_cart()
        time.sleep(0.5)
        self.cartpage_object.go_to_checkout_page()
        time.sleep(1)
        self.checkoutpage_object.select_cash_payment()
        self.checkoutpage_object.send_comments("Testing coment 1")
        time.sleep(3)
        self.checkoutpage_object.select_tips_on_receipt_chose_amount(12)
        # self.checkoutpage_object.send_the_order()
#Activating last line of this test and running with the line active, the order will be made


    def test_finish_a_different_order_process(self):
        self.homepage_object.setup_intro_cookies_and_location()
        self.homepage_object.log_in()
        self.homepage_object.go_to_salads_from_menu_dropdown_list()
        time.sleep(2)
        self.saladspage_object.add_Caesar_salad_to_cart()
        self.itempage_object.select_Caesar_dressing()
        self.itempage_object.add_the_product_to_cart()
        time.sleep(2)
        self.homepage_object.go_to_desert_from_menu_dropdown_list()
        self.desertpage_object.select_brownie_desert()
        time.sleep(2)
        self.itempage_object.add_the_product_to_cart()
        time.sleep(4)
        self.desertpage_object.select_strawberry_desert()
        time.sleep(3)
        self.homepage_object.go_to_drinks_from_menu_dropdown_list()
        self.homepage_object.click_on_My_Account()
        time.sleep(3)
        self.drinkpage_object.select_apa_minerala_option()
        time.sleep(2)
        self.itempage_object.add_the_product_to_cart()
        time.sleep(1)
        self.cartpage_object.go_to_checkout_page()
        time.sleep(1)
        self.checkoutpage_object.select_card_arrival_payment()
        self.checkoutpage_object.send_comments("Testing coment 2")
        time.sleep(3)
        self.checkoutpage_object.select_tips_on_receipt_five_percent()
        # self.checkoutpage_object.send_the_order()
# Activating last line of this test and running with the line active, the order will be made

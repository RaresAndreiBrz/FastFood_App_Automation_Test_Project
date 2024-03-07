import time

from Locators.salads_page_locs import SaladsPageLocators
from Pages.base_page import BasePage


class SaladsPage(BasePage):

    def __init__(self) -> None:
        pass

    def check_presence_of_more_than_three_products_displayed_on_page(self):
        products_on_page = self.driver.find_elements(*SaladsPageLocators.products_listed_on_page)
        assert len(products_on_page) > 3, "Expected more than 3 and less than 3 are displayed"

    def check_Tuna_Salad_is_available(self):
        assert self.driver.find_element(*SaladsPageLocators.salad_Tuna_btn).is_displayed(), "Tuna Salad not displayed, expected otherwise"

    def check_Home_Salad_is_available(self):
        assert self.driver.find_element(*SaladsPageLocators.salad_Home_btn).is_displayed(), "'Home' Salad not displayed, expected otherwise"

    def check_Caesar_Salad_is_available(self):
        assert self.driver.find_element(
            *SaladsPageLocators.salad_Caesar_btn).is_displayed(), "Caesar Salad not displayed, expected otherwise"

    def check_Veggie_Salad_is_available(self):
        assert self.driver.find_element(
            *SaladsPageLocators.salad_Veggie_btn).is_displayed(), "Veggie Salad not displayed, expected otherwise"

    def check_short_intro_of_all_products(self):
        elem1 = self.driver.find_element(*SaladsPageLocators.informations_boxes1)
        elem2 = self.driver.find_element(*SaladsPageLocators.informations_boxes2)
        elem3 = self.driver.find_element(*SaladsPageLocators.informations_boxes3)
        elem4 = self.driver.find_element(*SaladsPageLocators.informations_boxes4)
        elem5 = self.driver.find_element(*SaladsPageLocators.informations_boxes5)
        elem6 = self.driver.find_element(*SaladsPageLocators.informations_boxes6)
        texts = elem1.text+elem2.text+elem3.text+elem4.text+elem5.text+elem6.text
        print(texts)
        assert "Salata, rosii, " in texts, "Text not present in description"
        assert "cedar, crutoane si dressing" in texts, "Text not present in description"
        assert " dressing Caesar, Vinaigrette" in texts, "Text not present in description"
        assert "Vinaigrette sau 1000 Island" in texts, "Text not present in description"
        assert "porumb, masline, cedar, rosii, crutoane si dressing Caesar, Vinaigrette" in texts, "Text not present in description"
        assert "1 salata + 1 portie de Wedges sau Rings + 1 sos" in texts, "Text not present in description"

    def check_informations_button_of_a_salad(self):
        self.driver.find_element(*SaladsPageLocators.info_button_of_Mediterana_salad).click()
        time.sleep(0.5)
        assert self.driver.find_element(*SaladsPageLocators.ingredients_btn_of_Medit_salad).is_displayed(), 'Ingredients info is not present'

    def add_Caesar_salad_to_cart(self):
        self.driver.find_element(*SaladsPageLocators.salad_Caesar_btn).click()
        time.sleep(1)

import time

from Locators.calzone_page_locs import CalzonePageLocators
from Pages.base_page import BasePage


class CalzonePage(BasePage):

    def __init__(self) -> None:
        pass

    def select_calzone_option(self):
        self.driver.find_element(*CalzonePageLocators.simple_calzone).click()
        time.sleep(0.2)

    def select_menu_calzone_option(self):
        self.driver.find_element(*CalzonePageLocators.menu_calzone).click()
        time.sleep(0.2)

    def take_price_of_calzone_displayed_on_page(self):
        price_text = self.driver.find_element(*CalzonePageLocators.price_of_product_text_btn).text
        for char in price_text:
            if char not in '0123456789.':
                price_text = price_text.replace(char, '')
        result = float(price_text) if price_text else None
        return result


    def check_more_than_one_product_is_displayed_on_page(self):
        products = self.driver.find_elements(*CalzonePageLocators.products_listed_on_page)
        assert len(products) > 1, "Less than two products are displayed. Expected more than one"

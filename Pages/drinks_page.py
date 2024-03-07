import time

from Locators.drinks_page_locs import DrinksPageLocators
from Locators.item_page_locs import ItemPageLocators
from Pages.base_page import BasePage


class DrinksPage(BasePage):

    def __init__(self) -> None:
        pass


    def select_fanta_option(self):
        for i in range(10):
            try:
                self.driver.find_element(*DrinksPageLocators.fanta_btn).click()
                if self.driver.find_element(*ItemPageLocators.add_to_cart_second_btn).is_displayed:
                    break
            except:
                pass
        time.sleep(0.2)

    def select_apa_plata_option(self):
        for i in range(10):
            try:
                self.driver.find_element(*DrinksPageLocators.water_btn).click()
                if self.driver.find_element(*ItemPageLocators.add_to_cart_second_btn).is_displayed:
                    break
            except:
                pass
        time.sleep(0.2)
    def select_apa_minerala_option(self):
        for i in range(10):
            try:
                self.driver.find_element(*DrinksPageLocators.sprinkle_water_btn).click()
                if self.driver.find_element(*ItemPageLocators.add_to_cart_second_btn).is_displayed:
                    break
            except:
                pass
        time.sleep(0.2)
    def select_redbull_option(self):
        for i in range(10):
            try:
                self.driver.find_element(*DrinksPageLocators.redbull_btn).click()
                if self.driver.find_element(*ItemPageLocators.add_to_cart_second_btn).is_displayed:
                    break
            except:
                pass

    def add_product_to_cart_after_selected_quantity(self):
        self.driver.find_element(*DrinksPageLocators.add_to_cart_second_btn).click()

    def add_product_to_favorite(self):
        self.driver.find_element(*DrinksPageLocators.add_favorite_btn).click()

    def select_quantity(self, smallest_to_highest_int):
        if smallest_to_highest_int == 1:
            self.driver.find_element(*ItemPageLocators.cola_quantity_330_btn).click()
        elif smallest_to_highest_int == 2:
            self.driver.find_element(*ItemPageLocators.cola_quantity_05_btn).click()
        elif smallest_to_highest_int == 3:
            self.driver.find_element(*ItemPageLocators.cola_quantity_2_btn).click()
        else:
            pass

    def send_comments(self, your_comment_here):
        self.driver.find_element(*ItemPageLocators.comments_btn).send_text(str(your_comment_here))

    def cancel_product_selection(self):
        self.driver.find_element(*ItemPageLocators.cancel_product_panel_btn).click()

    def total_price_text(self):
        price = self.driver.find_element(*DrinksPageLocators.total_price_text_btn)
        price_text = price.text.replace(" ", "").replace("lei", "")
        return price_text
    def total_products_on_page(self):
        list_products = self.driver.find_elements(*DrinksPageLocators.products_listed_on_page)
        return len(list_products)

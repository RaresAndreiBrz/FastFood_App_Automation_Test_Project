import time

from Locators.cart_page_locs import CartPageLocators
from Pages.base_page import BasePage


class CartPage(BasePage):

    def __init__(self) -> None:
        pass

    def click_on_cart_btn(self):
        time.sleep(0.3)
        self.driver.find_element(*CartPageLocators.cart_btn).click()
        time.sleep(2)

    def add_quantity(self, index_of_product_in_cart, int_multiplier):
        list_products = self.driver.find_element(*CartPageLocators.increase_quantity_popUp_cart_btn)
        product_selected = list_products[index_of_product_in_cart]
        for i in range(int_multiplier):
            try:
                product_selected.click()
            except:
                pass

    def reduce_quantity(self, index_of_product_in_cart, int_multiplier):
        list_products = self.driver.find_element(*CartPageLocators.decrease_quantity_popUp_cart_btn)
        product_selected = list_products[index_of_product_in_cart]
        for i in range(int_multiplier):
            try:
                product_selected.click()
            except:
                pass

    def check_number_of_products_in_cart(self, number_of_products_you_added):
        number_of_products_in_cart = self.driver.find_element(*CartPageLocators.number_displayed_on_popUp_cart)
        print(number_of_products_in_cart)
        print(number_of_products_you_added)
        assert int(number_of_products_you_added) == int(number_of_products_in_cart.text), "Numbers are not equal, as expected"

    def click_on_finish_order_in_cart(self):
        currenturl = "url removed"
        while self.driver.current_url == currenturl:
            btn = self.wait_for_clickable_element(CartPageLocators.finish_order_btn)
            btn.click()

    def go_to_checkout_page(self):
        self.click_on_cart_btn()
        self.click_on_finish_order_in_cart()
        time.sleep(5)

    def delete_product_from_popUp_cart(self):
        self.driver.find_element(*CartPageLocators.remove_product_from_popUp_cart_btn).click()

    def remove_first_product_from_cart(self):
        self.driver.find_element(*CartPageLocators.first_product_remove_btn).click()

    def remove_second_product_from_cart(self):
        self.driver.find_element(*CartPageLocators.second_product_remove_btn).click()

    def remove_third_product_from_cart(self):
        self.driver.find_element(*CartPageLocators.third_product_remove_btn).click()

    def remove_fourth_product_from_cart(self):
        self.driver.find_element(*CartPageLocators.fourth_product_remove_btn).click()

    def remove_fifth_product_from_cart(self):
        self.driver.find_element(*CartPageLocators.fifth_product_remove_btn).click()

    def remove_sixth_product_from_cart(self):
        self.driver.find_element(*CartPageLocators.sixth_product_remove_btn).click()



    def take_price_of_calzone_displayed_on_cart(self):
        price_text = self.driver.find_element(*CartPageLocators.price_of_first_product).text
        for char in price_text:
            if char not in '0123456789.':
                price_text = price_text.replace(char, '')
        result = float(price_text) if price_text else None
        return result

    def price_of_all_products(self):
        price = self.driver.find_element(*CartPageLocators.price_of_total_products)
        price_text = price.text.replace(" ", "").replace("lei", "")
        return price_text

    def get_number_of_products_in_cart(self):
        number_of_products_in_cart = self.driver.find_element(*CartPageLocators.number_of_products_in_cart).text
        return int(number_of_products_in_cart)

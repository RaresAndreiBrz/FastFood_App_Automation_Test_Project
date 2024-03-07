import random
import time

from Locators.item_page_locs import ItemPageLocators
from Pages.base_page import BasePage


class ItemPage(BasePage):

    def add_the_product_to_cart(self):
        self.driver.find_element(*ItemPageLocators.add_to_cart_second_btn).click()
        time.sleep(0.5)

    def cancel_cart_panel(self):
        self.driver.find_element(*ItemPageLocators.cancel_product_panel_btn).click()

    def select_dough_integral(self):
        self.driver.find_element(*ItemPageLocators.dough_integral_btn).click()

    def select_dough_fluffy(self):
        self.driver.find_element(*ItemPageLocators.dough_fluffy_btn).click()

    def select_dough_thin(self):
        self.driver.find_element(*ItemPageLocators.dough_thin_btn).click()

    def select_ss_sweet_bbq(self):
        self.driver.find_element(*ItemPageLocators.ss_bbq_dulce_btn).click()

    def select_ss_hot_bbq(self):
        self.driver.find_element(*ItemPageLocators.ss_bbq_iute_btn2).click()

    def select_ss_chili(self):
        self.driver.find_element(*ItemPageLocators.ss_chili_btn).click()

    def select_ss_salsa(self):
        self.driver.find_element(*ItemPageLocators.ss_salsa_btn).click()

    def select_ss_tabasco(self):
        self.driver.find_element(*ItemPageLocators.ss_tabasco_btn).click()

    def select_ss_mustard(self):
        self.driver.find_element(*ItemPageLocators.ss_mustard_btn).click()

    def select_ss_pizza(self):
        self.driver.find_element(*ItemPageLocators.ss_pizza_btn).click()

    def select_ss_garden(self):
        self.driver.find_element(*ItemPageLocators.ss_garden_btn).click()

    def select_extra_sos_bbq_sweet(self):
        self.driver.find_element(*ItemPageLocators.extra_ss_bbq_sweet_btn).click()

    def select_toping_pineapple(self):
        self.driver.find_element(*ItemPageLocators.topping_pineapple_btn).click()

    def select_toping_onion(self):
        self.driver.find_element(*ItemPageLocators.topping_onion_btn).click()

    def select_toping_cheese(self):
        self.driver.find_element(*ItemPageLocators.topping_cheese_btn).click()

    def select_toping_bacon(self):
        self.driver.find_element(*ItemPageLocators.topping_bacon_btn).click()

    def select_toping_wedges(self):
        self.driver.find_element(*ItemPageLocators.topping_wedges_btn).click()

    def select_toping_tuna(self):
        self.driver.find_element(*ItemPageLocators.topping_tuna_btn).click()

    def select_toping_chicken(self):
        self.driver.find_element(*ItemPageLocators.topping_chicken_btn).click()

    def select_no_mozzarella(self):
        self.driver.find_element(*ItemPageLocators.no_mozzarella_btn).click()

    def select_no_corn(self):
        self.driver.find_element(*ItemPageLocators.no_corn_btn).click()

    def select_better_baked(self):
        self.driver.find_element(*ItemPageLocators.better_baked_btn).click()

    def select_less_baked(self):
        self.driver.find_element(*ItemPageLocators.less_baked_btn).click()

    def select_freeDrink_water(self):
        self.driver.find_element(*ItemPageLocators.water_option_for_menu).click()

    def send_comments(self, your_comment):
        self.driver.find_element(ItemPageLocators.comments_btn).send_keys(f"{your_comment}")

    def select_three_random_toppings_for_calzone(self, min_three_max_seven_choices_toppings):
        toppings = [self.select_toping_onion, self.select_toping_pineapple, self.select_toping_bacon,
                    self.select_toping_chicken, self.select_toping_tuna, self.select_toping_wedges,
                    self.select_toping_cheese]

        selected_toppings = random.sample(toppings, min_three_max_seven_choices_toppings)
        for topg in selected_toppings:
            topg()

    def fully_add_calzone_details_to_pruchase(self):
        time.sleep(1)
        self.select_ss_pizza()
        self.select_three_random_toppings_for_calzone(3)
        self.select_better_baked()
        self.add_the_product_to_cart()

    def select_Caesar_dressing(self):
        self.driver.find_element(*ItemPageLocators.dressing_Caesar_btn).click()

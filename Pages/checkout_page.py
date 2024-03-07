import time

from selenium.webdriver import ActionChains

from Locators.checkout_page_locs import CheckoutPageLocators
from Pages.base_page import BasePage


class CheckoutPage(BasePage):

    def __init__(self) -> None:
        pass

    def check_presence_of_checkout_page(self):
        time.sleep(3)
        title = self.driver.find_element(*CheckoutPageLocators.title_of_checkout_page)
        assert title.text == "Plaseaza comanda", "Different text expected"

    def select_cash_payment(self):
        self.driver.find_element(*CheckoutPageLocators.chose_payment_method_btn).click()
        self.driver.find_element(*CheckoutPageLocators.pay_cash_btn).click()
        time.sleep(5)


    def select_card_arrival_payment(self):
        self.driver.find_element(*CheckoutPageLocators.chose_payment_method_btn).click()
        self.driver.find_element(*CheckoutPageLocators.pay_card_on_delivery_btn).click()

    def send_comments(self, your_comment):
        self.driver.find_element(*CheckoutPageLocators.comments_btn).click()
        actions = ActionChains(self.driver)
        actions.send_keys(f"{your_comment}").perform()

    def select_tips_on_receipt_five_percent(self):
        self.driver.find_element(*CheckoutPageLocators.tips_5_perc_btn).click()

    def select_tips_on_receipt_ten_percent(self):
        self.driver.find_element(*CheckoutPageLocators.tips_10_perc_btn).click()

    def select_tips_on_receipt_fifteen_percent(self):
        self.driver.find_element(*CheckoutPageLocators.tips_15_perc_btn).click()

    def select_tips_on_receipt_chose_amount(self, amount):
        self.driver.find_element(*CheckoutPageLocators.tips_chose_amount_btn).click()
        time.sleep(0.1)
        self.driver.find_element(*CheckoutPageLocators.tips_input_amount_section).click()
        actions = ActionChains(self.driver)
        actions.send_keys(f"{amount}").perform()
        self.driver.find_element(*CheckoutPageLocators.tips_save_wrote_amount_btn).click()

    def send_the_order(self):
        self.driver.find_element(*CheckoutPageLocators.send_order_btn).click()

    def add_invalid_promotional_code_and_check_result(self, promo_code):
        self.driver.find_element(*CheckoutPageLocators.discount_code_btn1).click()
        time.sleep(0.2)
        self.driver.find_element(*CheckoutPageLocators.discount_code_btn2).click()
        time.sleep(0.2)
        input_area = self.driver.find_element(*CheckoutPageLocators.input_discount_code_btn3)
        input_area.click()
        input_area.send_keys(promo_code)
        time.sleep(0.2)
        self.driver.find_element(*CheckoutPageLocators.apply_discount_code_btn).click()
        time.sleep(4)
        assert self.driver.find_element(*CheckoutPageLocators.discount_alert).is_displayed(), "Alert does not show up as expected"



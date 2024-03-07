import time

from selenium.webdriver import ActionChains

from Locators.checkout_page_locs import CheckoutPageLocators
from Locators.sausage_page_locs import SausagePageLocators
from Pages.base_page import BasePage


class SausagePage(BasePage):

    def __init__(self) -> None:
        pass

    def check_presence_of_sausage_page(self):
        sausage_url = "url removed"
        assert self.driver.current_url == sausage_url, f"Expected {sausage_url}, and {self.driver.current_url} showed up"

    def select_bbq_ss(self):
        for i in range(12):
            try:
                self.driver.find_element(*SausagePageLocators.bbq_ss).click()
            except:
                pass
        time.sleep(0.2)


import time

from Locators.calzone_page_locs import CalzonePageLocators
from Locators.desert_page_locs import DesertPageLocators
from Pages.base_page import BasePage


class DesertPage(BasePage):

    def __init__(self) -> None:
        pass

    def select_brownie_desert(self):
        self.driver.find_element(*DesertPageLocators.brownie_btn).click()
        time.sleep(0.2)

    def select_pistachio_desert(self):
        self.driver.find_element(*DesertPageLocators.pistachio_btn).click()
        time.sleep(0.2)

    def select_cinnamon_desert(self):
        self.driver.find_element(*DesertPageLocators.cinnamon_btn).click()
        time.sleep(0.2)

    def select_strawberry_desert(self):
        self.driver.find_element(*DesertPageLocators.strawberry_btn).click()
        time.sleep(0.2)

    def select_cherry_desert(self):
        self.driver.find_element(*DesertPageLocators.cherry_btn).click()
        time.sleep(0.2)


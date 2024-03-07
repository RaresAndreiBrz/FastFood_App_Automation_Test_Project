import unittest

from Pages.about_products_page import AboutProductsPage
from Pages.base_page import BasePage
from Pages.calzone_page import CalzonePage
from Pages.cart_page import CartPage
from Pages.checkout_page import CheckoutPage
from Pages.desert_page import DesertPage
from Pages.drinks_page import DrinksPage
from Pages.homepage import Homepage
from Pages.item_page import ItemPage
from Pages.jobs_page import JobsPage
from Pages.news_page import NewsPage
from Pages.salads_page import SaladsPage
from Pages.sausage_page import SausagePage


class BaseTests(BasePage,unittest.TestCase):

    def setUp(self) -> None:

        self.homepage_object = Homepage()
        self.calzonepage_object = CalzonePage()
        self.cartpage_object = CartPage()
        self.itempage_object = ItemPage()
        self.checkoutpage_object = CheckoutPage()
        self.drinkpage_object = DrinksPage()
        self.desertpage_object = DesertPage()
        self.jobspage_object = JobsPage()
        self.aboutprod_object = AboutProductsPage()
        self.newspage_object = NewsPage()
        self.saladspage_object = SaladsPage()
        self.sausagespage_object = SausagePage()
        self.driver.get('MAIN URL REMOVED')
        self.driver.maximize_window()
        self.driver.set_script_timeout(10)


    def tearDown(self):
        self.driver.quit()


    def back(self):
        self.driver.back()


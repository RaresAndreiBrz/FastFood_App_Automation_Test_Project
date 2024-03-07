from Locators.about_products_page_locs import AboutProductsPageLocators
from Pages.base_page import BasePage


class AboutProductsPage(BasePage):

    def __init__(self) -> None:
        pass

    def check_if_page_title_is_displayed(self):
        self.driver.find_element(
            *AboutProductsPageLocators.title_of_the_page).is_displayed(), "Title 'Despre Produse' should have been found, but not seen on the page"

    def check_if_product_pizza_is_displayed(self):
        assert self.driver.find_element(*AboutProductsPageLocators.pizza_title).is_displayed(), 'Product "Pizza" should have been on the page'

    def check_if_pizza_description_is_available(self):
        list_items_in_text = ["Tipuri de blat", "Blatul clasic", "blat crocant", "faină integrală 100%",
                              "sosul de tomate", "multele topping-uri disponibile"]
        text_box = self.driver.find_element(*AboutProductsPageLocators.pizza_text)
        assert text_box.is_displayed(), "Description of the product 'Pizza' should have been present"
        for item in list_items_in_text:
            assert item in text_box.text, f"Topic '{item}' is missing from description"

    def check_if_product_calzonee_is_displayed(self):
        assert self.driver.find_element(
            *AboutProductsPageLocators.calzone_title).is_displayed(), "Product 'Calzone' should have been on the page"

    def check_if_calzone_description_is_available(self):
        list_items_in_text = ["ca un portofel", "toppinguri (2-3)", "blat de pizza de 25cm", "blat ușor crocant și rumen",
                              "amestec de făină și oregano", "maxim 3 topping-uri la alegere."]
        text_box = self.driver.find_element(*AboutProductsPageLocators.calzone_text)
        assert text_box.is_displayed(), "Description of the product 'Calzone' should have been present"
        for item in list_items_in_text:
            assert item in text_box.text, f"Topic '{item}' is missing from description"

    def check_if_product_stripwich_is_displayed(self):
        assert self.driver.find_element(
            *AboutProductsPageLocators.stripwich_title).is_displayed(), 'Product "Stripwich" should have been on the page'

    def check_if_stripwich_description_is_available(self):
        list_items_in_text = ["produs propriu", "altfel de sandwich", "blat cu oregano, copt și rumenit în cuptor,",
                              "Stripwich cu Pui",
                              "Stripwich cu Șuncă", "Stripwich cu Ton:"]
        text_box = self.driver.find_element(*AboutProductsPageLocators.stripwich_text)
        assert text_box.is_displayed(), "Description of the product 'Stripwich' should have been present"
        for item in list_items_in_text:
            assert item in text_box.text, f"Topic '{item}' is missing from description"

    def check_if_product_bbq_wings_is_displayed(self):
        assert self.driver.find_element(
            *AboutProductsPageLocators.bbq_title).is_displayed(), 'Product "Bbq Wings" should have been on the page'

    def check_if_bbq_wings_description_is_available(self):
        list_items_in_text = ["Buffalo Wings", "bucăți (secțiuni) de aripioare de pui",
                              "prăjire și ulterior acoperire cu un sos variabil de picant",
                              "prăjire, coacere la cuptor sau pe grătar",
                              "preprăjire scurtă la temperatură mare", "6 bucăți sau de 10"]
        text_box = self.driver.find_element(*AboutProductsPageLocators.bbq_text)
        assert text_box.is_displayed(), "Description of the product 'Bbq Wings' should have been present"
        for item in list_items_in_text:
            assert item in text_box.text, f"Topic '{item}' is missing from description"


    def check_if_product_pasta_is_displayed(self):
        self.wait_for_displayed_element(AboutProductsPageLocators.pasta_title)
        assert self.driver.find_element(
            *AboutProductsPageLocators.pasta_title).is_displayed(), 'Product "Pasta" should have been on the page'

    def check_if_pasta_description_is_available(self):
        list_items_in_text = [" 4 dintre cele mai populare sosuri în care să preparăm pastele tip pene", "bucățele de vită și usturoi proaspăt",
                              "roșii pulpă, busuioc și ulei de măsline",
                              "dovlecei, vinete, ardei roșu și ceapă",
                              " la cerere, și rondele propaspete de ardei", "gratinate cu mozzarella"]
        text_box = self.driver.find_element(*AboutProductsPageLocators.pasta_text)
        assert text_box.is_displayed(), "Description of the product 'Pasta' should have been present"
        for item in list_items_in_text:
            assert item in text_box.text, f"Topic '{item}' is missing from description"

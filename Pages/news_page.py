import time

from selenium.webdriver import ActionChains

from Locators.checkout_page_locs import CheckoutPageLocators
from Locators.news_page_locs import NewsPageLocators
from Pages.base_page import BasePage


class NewsPage(BasePage):



    def __init__(self) -> None:
        pass

    def check_presence_of_news_page(self):
        expected_url = "URL REMOVED"
        self.driver.current_url == expected_url, f"Expected {expected_url}, insteaeed received {self.driver.current_url}"

    def check_presence_of_last_news_subject_Cluj(self):
        assert self.driver.find_element(*NewsPageLocators.news_1_box).is_displayed(), "Last news does not show up as expected."
        dates = self.driver.find_elements(*NewsPageLocators.dates_of_all_news)
        assert dates[0].text == "11 Nov 2022, 13:15"

    def check_multiple_news_are_displayed(self):
        assert len(self.driver.find_elements(*NewsPageLocators.dates_of_all_news)) > 2, "Less than 2 news are displayed on page, and more than 3 were expected"

    def check_introductions_of_news_texts_are_displayed(self):
        news_intro = self.driver.find_element(*NewsPageLocators.news_3_introduction).text
        assert "magazin este situat central, pe Calea București" in news_intro, "Part of introduction section is not displayed, as expected"

    def news_contains_image(self):
        img = self.driver.find_element(*NewsPageLocators.news_5_img)
        assert img.is_displayed(), "An image was expected to be present, and the result shows that is not."

    def news_contains_multiple_images(self):
        imgs = self.driver.find_elements(*NewsPageLocators.news_imgs)
        assert len(imgs) > 44, "Over 44 images were expected and less than 44 shows up."

    def check_time_corresponds_in_between_pages(self):
        date1 = self.driver.find_element(*NewsPageLocators.news7_newspage_date).text
        print(date1)
        for i in range(10):
            try:
               self.driver.find_element(*NewsPageLocators.news_7_box).click()
            except:
                pass
        time.sleep(5)
        date2 = self.driver.find_element(*NewsPageLocators.news7_date).text
        assert date1 == date2, "The dates displayed on news page of a story doesnt match with the story`s inside date."

    def check_date_of_story_displayed_only_once(self):
        dates = self.driver.find_elements(*NewsPageLocators.dates_of_all_news)
        date_texts = [date.text for date in dates]
        date_of_third_story = dates[2].text
        assert date_texts.count(date_of_third_story) == 1, "The date of the third story shows up more than once, while no more than once was expected"
        assert len(date_texts) == len(set(date_texts))

    def check_informations_of_fifth_story_are_displayed(self):
        for i in range(25):
            try:
                self.driver.find_element(*NewsPageLocators.news_5_box).click()
            except:
                pass
        time.sleep(7)
        assert self.driver.find_element(*NewsPageLocators.story_of_the_news5).is_displayed(), "Informations are not displayed, as expected"

    def check_name_of_the_first_story_is_correctly_displayed(self):
        time.sleep(5)
        name1 = self.driver.find_element(*NewsPageLocators.news_1_box_title).text
        time.sleep(5)
        for i in range(8):
            try:
                self.driver.find_element(*NewsPageLocators.news_1_box).click()
            except:
                pass
        time.sleep(5)
        name2 = self.driver.find_element(*NewsPageLocators.news1_title_inside).text
        text = "removed NEWS TITLE"
        assert text in name1, "Title names are different, expected to be the same."
        assert text in name2, "Title names are different, expected to be the same."

    def check_images_displayed_on_ninth_story(self):
        time.sleep(6)
        for i in range(10):
            try:
                self.driver.find_element(*NewsPageLocators.news_9_box).click()
            except:
                pass

        time.sleep(6)
        img_elem = self.driver.find_element(*NewsPageLocators.first_img)
        img_src = img_elem.get_attribute("src")
        assert img_src and "data:image" not in img_src, "Image is not displayed, as expected"

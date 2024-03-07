from selenium.webdriver.common.by import By



class CalzonePageLocators:

    price_of_product_text_btn = (By.XPATH, "(//button[@class='btn btn-outline-info'])[1]")
    products_listed_on_page = (By.XPATH, "(//div[@class='col'])")

    simple_calzone = (By.XPATH, "(//button[@class='btn btn-outline-info'])[1]")
    menu_calzone = (By.XPATH, "(//button[@class='btn btn-outline-info'])[2]")

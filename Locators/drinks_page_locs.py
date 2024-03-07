from selenium.webdriver.common.by import By


class DrinksPageLocators:


    add_favorite_btn = (By.XPATH, "(//button[@class='btn btn-outline-primary'])[1]")
    add_to_cart_second_btn = (By.XPATH, "//button[@class='btn shadow-lg btn-primary']")
    total_price_text_btn = (By.XPATH, "(//div[@class='ms-2 d-flex flex-column'])[1]")
    products_listed_on_page = (By.XPATH, "(//div[@class='col'])")

    fanta_btn = (By.XPATH, '//*[@id="__next"]/div[2]/div/div[2]/div/div[4]/div/div[1]/a/span/img')
    water_btn = (By.XPATH, '//*[@id="__next"]/div[2]/div/div[2]/div/div[7]')
    sprinkle_water_btn = (By.XPATH, '//*[@id="__next"]/div[2]/div/div[2]/div/div[8]')
    redbull_btn = (By.XPATH, '//*[@id="__next"]/div[2]/div/div[2]/div/div[9]/div/div[1]/a/span/img')


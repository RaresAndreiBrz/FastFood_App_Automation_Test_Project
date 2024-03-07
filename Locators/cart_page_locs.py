from selenium.webdriver.common.by import By


class CartPageLocators:

    # cart button details
    cart_btn = (By.XPATH, "(//button[@class='btn btn-white position-relative me-3 d-none d-xl-block'])[1]")
    number_of_products_in_cart = (By.CSS_SELECTOR,
                                  "button[class='btn btn-white position-relative me-3 d-none d-xl-block'] span[class='position-absolute top-0 start-1 translate-middle badge rounded-pill bg-primary']")
    number_displayed_on_the_homepg_cart = (By.XPATH, '//*[@id="navbarMenu"]/div/button/span')
    number_displayed_on_popUp_cart = (By.XPATH, '/html/body/div/div[2]/header/nav/div/div[3]/div/button/span')


    # in cart buttons
    decrease_quantity_popUp_cart_btn = (By.XPATH, "//button[normalize-space()='-']")
    increase_quantity_popUp_cart_btn = (By.XPATH, "//button[normalize-space()='+']")
    remove_product_from_popUp_cart_btn = (By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div[1]/div/div/div[6]/div[2]/button")
    finish_order_btn = (By.XPATH, '//button[normalize-space()="Finalizeaza comanda"]')
    price_of_total_products = (By.XPATH, "(//span[@class='text-primary'])[1]")
    price_of_first_product = (By.XPATH, '//span[@class="fw-bold"][normalize-space()="29.75 lei"]')

    # remove buttons
    first_product_remove_btn = (By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div[1]/div/div/div[6]/div[2]/button")
    second_product_remove_btn = (By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div[2]/div/div/div[5]/div[2]/button")
    third_product_remove_btn = (By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div[3]/div/div/div[5]/div[2]/button")
    fourth_product_remove_btn = (By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div[4]/div/div/div[5]/div[2]/button")
    fifth_product_remove_btn = (By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div[5]/div/div/div[5]/div[2]/button")
    sixth_product_remove_btn = (By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div[6]/div/div/div[5]/div[2]/button")

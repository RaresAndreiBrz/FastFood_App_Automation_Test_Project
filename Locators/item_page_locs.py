from selenium.webdriver.common.by import By


class ItemPageLocators:
    total_price_text_btn = (By.XPATH, "(//div[@class='ms-2 d-flex flex-column'])[1]")
    comments_btn = (By.XPATH, "(//label[normalize-space()='Comentarii'])[1]")
    cancel_product_panel_btn = (By.XPATH,
                                "//button[@class='MuiButtonBase-root MuiIconButton-root MuiIconButton-colorSecondary MuiIconButton-sizeLarge position-absolute top-0 end-0 css-1qlbe7']")
    add_to_cart_second_btn = (By.XPATH, "//button[@class='btn shadow-lg btn-primary']")

    dough_thin_btn = (By.XPATH, "/html/body/div[3]/div/div/div[1]/div/div[2]/div[1]/div[2]/div[2]/div[2]/div")
    dough_fluffy_btn = (By.XPATH, "")
    dough_integral_btn = (By.XPATH, "/html/body/div[3]/div/div/div[1]/div/div[2]/div[1]/div[2]/div[2]/div[3]/div")

    ss_bbq_dulce_btn = (By.XPATH, "/html/body/div[3]/div/div/div[1]/div/div[2]/div[1]/div[2]/div[2]/div[1]/div")
    ss_bbq_iute_btn2 = (By.XPATH, "(//div[contains(text(),'Iute')])[1]")
    ss_salsa_btn = (By.XPATH, "(//div[contains(text(),'salsa')])[1]")
    ss_garden_btn = (By.XPATH, "(//div[@class='col'][1])")
    ss_pizza_btn = (By.XPATH, "(//div[@class='col'][3])")
    ss_chili_btn = (By.XPATH, "(//div[@class='col'][5])")
    ss_mustard_btn = (By.XPATH, "(//div[@class='col'][6])")
    ss_tabasco_btn = (By.XPATH, "(//div[@class='col'][7])")
    extra_ss_bbq_sweet_btn = (By.XPATH, "/html/body/div[3]/div/div/div[1]/div/div[2]/div[1]/div[5]/div[2]/div[1]/div")

    topping_pineapple_btn = (By.XPATH, "(//div[contains(text(),'ananas')])[1]")
    topping_chicken_btn = (By.XPATH, "(//div[contains(text(),'pui')])[1]")
    topping_tuna_btn = (By.XPATH, "(//div[contains(text(),'ton')])[1]")
    topping_wedges_btn = (By.XPATH, "/html/body/div[3]/div/div/div[1]/div/div[2]/div[1]/div[3]/div[2]/div[22]/div")
    topping_bacon_btn = (By.XPATH, "(//div[contains(text(),'bacon')])[1]")
    topping_cheese_btn = (By.XPATH, "(//div[contains(text(),'telemea')])[1]")
    topping_onion_btn = (
        By.XPATH,
        "(//div[@class='d-flex align-items-left text-start flex-column gap-1'][normalize-space()='ceapa'])[1]")

    no_corn_btn = (By.XPATH, "(//div[contains(text(),'fara malai')])[1]")
    no_mozzarella_btn = (By.XPATH, "(//div[contains(text(),'fara mozzarella')])[1]")
    better_baked_btn = (By.XPATH, "(//div[contains(text(),'mai bine coapta')])[1]")
    less_baked_btn = (By.XPATH, "(//div[contains(text(),'mai putin coapta')])[1]")

    cola_quantity_05_btn = (By.XPATH, "/html/body/div[3]/div/div/div[1]/div/div[2]/div[1]/div/div[2]/div[1]/div")
    cola_quantity_2_btn = (By.XPATH, '/html/body/div[3]/div/div/div[1]/div/div[2]/div[1]/div/div[2]/div[1]/div')
    cola_quantity_330_btn = (By.XPATH, '/html/body/div[3]/div/div/div[1]/div/div[2]/div[1]/div/div[2]/div[1]/div')

    dressing_island_btn = (
        By.XPATH, "//body[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]")
    dressing_Caesar_btn = (
        By.XPATH, "//body[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]")
    dressing_none_btn = (
        By.XPATH, "//body[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[3]/div[1]")
    dressing_vinnaigrette_btn = (
        By.XPATH, "//body[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[4]/div[1]")

    extra_dressing_noExtra_btn = (
        By.XPATH, "//body[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[2]/div[1]/div[1]")
    extra_dressing_island_btn = (
        By.XPATH, "//body[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[2]/div[2]/div[1]")
    extra_dressing_Caesar_btn = (
        By.XPATH, "//body[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[2]/div[3]/div[1]")
    extra_dressing_vinnaigrette_btn = (
        By.XPATH, "//body[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[2]/div[4]/div[1]")

    mLight_ss_bbq_dulce_btn = (By.XPATH,
                                   "(//div[@class='d-flex align-items-left text-start flex-column gap-1'][normalize-space()='bbq dulce'])[1]")
    mLight_ss_bbq_iute_btn = (By.XPATH, "(//div[contains(text(),'bbq iute')])[1]")
    mLight_ss_salsa_btn = (By.XPATH, "(//div[contains(text(),'salsa')])[1]")

    mLight_side_wedges_btn = (By.XPATH, "//div[contains(text(),'Cartofi wedges')]")
    mLight_side_onion_rings_btn = (By.XPATH, "(//div[contains(text(),'Inele de ceapa')])[1]")
    water_option_for_menu = (By.XPATH, "/html/body/div[3]/div/div/div[1]/div/div[2]/div[1]/div[4]/div[2]/div[1]/div")
    cola_option_for_menu = (By.XPATH, "/html/body/div[3]/div/div/div[1]/div/div[2]/div[1]/div[4]/div[2]/div[2]/div")
    cola_zero_option_for_menu = (By.XPATH, "/html/body/div[3]/div/div/div[1]/div/div[2]/div[1]/div[4]/div[2]/div[3]/div")
    fanta_option_for_menu = (By.XPATH, "/html/body/div[3]/div/div/div[1]/div/div[2]/div[1]/div[4]/div[2]/div[4]/div")
    sprite_option_for_menu = (By.XPATH, "/html/body/div[3]/div/div/div[1]/div/div[2]/div[1]/div[4]/div[2]/div[5]/div")


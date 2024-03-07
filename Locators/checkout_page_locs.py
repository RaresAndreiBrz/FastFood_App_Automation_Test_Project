from selenium.webdriver.common.by import By


class CheckoutPageLocators:
    title_of_checkout_page = (By.XPATH, '//*[@id="__next"]/div[2]/div/div[1]/h3')
    chose_payment_method_btn = (By.XPATH, "//body[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/button[1]")
    pay_cash_btn = (By.XPATH, "//li[normalize-space()='Plata numerar']")
    pay_card_on_delivery_btn = (By.XPATH, "//li[normalize-space()='Plata cu card la livrare']")
    discount_code_btn1 = (By.XPATH, '//button[normalize-space()="Aplica cod promo sau voucher"]')
    discount_code_btn2 = (By.XPATH, "(//button[normalize-space()='Adauga cod voucher'])[1]")
    input_discount_code_btn3 = (By.XPATH, '//input[@id="mui-8"]')
    apply_discount_code_btn = (By.XPATH, '//button[normalize-space()="Aplica cod"]')
    discount_alert = (By.XPATH, '//div[@role="alert"]')
    comments_btn = (By.XPATH,
                    "(//div[@class='MuiInputBase-root MuiOutlinedInput-root MuiInputBase-colorPrimary MuiInputBase-formControl MuiInputBase-multiline css-1e85jbm'])[1]")
    tips_5_perc_btn = (
        By.XPATH,
        "//body[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[6]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/button[1]")
    tips_10_perc_btn = (
        By.XPATH,
        "//body[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[6]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/button[1]")
    tips_15_perc_btn = (
        By.XPATH,
        "//body[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[6]/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/button[1]")
    tips_chose_amount_btn = (
        By.XPATH,
        "//body[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[6]/div[1]/div[1]/div[1]/div[2]/div[1]/div[4]/button[1]")
    tips_input_amount_section = (By.XPATH, '//input[@id="mui-10"]')
    tips_save_wrote_amount_btn = (By.XPATH, "//button[normalize-space()='Salveaza']")
    send_order_btn = (By.XPATH, "(//button[@id='mui-30'])[1]")

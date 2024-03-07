from selenium.webdriver.common.by import By


class HomepageLocators:


    #location buttons

    location_btn = (By.XPATH, "(//button[@type='button'][normalize-space()='Locatia: Bucuresti'])[1]")
    city_btn = (By.XPATH, '/html/body/div[4]/div/div/div[2]/div[1]/div/div/div/div')
    town_btn = (By.XPATH, '/html/body/div[4]/div/div/div[2]/div[2]/div/div/div/div')
    select_btn = (By.XPATH, "(//button[normalize-space()='Selecteaza'])[1]")

    #menu list buttons
    home_btn = (By.XPATH, "(//a[normalize-space()='Acasa'])[1]")
    menu_main_btn = (By.XPATH, '//*[@id="products-dropdown"]')
    offers_btn = (By.XPATH, "(//a[normalize-space()='Oferte'])[1]")
    shops_btn = (By.XPATH, '//*[@id="navbarMenu"]/ul/li[4]/a')
    about_btn = (By.XPATH, "(//a[normalize-space()='Despre'])[1]")


    #sub-menu buttons

    logo = (By.XPATH, '//*[@id="__next"]/div[2]/header/nav/div/div[1]/a/span/img')
    budget_dropdown_btn = (By.XPATH, '//*[@id="navbarMenu"]/ul/li[2]/ul/li[1]/a')
    offers_dropdown_btn = (By.XPATH, '//*[@id="navbarMenu"]/ul/li[2]/ul/li[2]/a')
    loyalty_dropdown_btn = (By.XPATH, '//*[@id="navbarMenu"]/ul/li[2]/ul/li[3]/a')
    pizza_dropdown_btn = (By.XPATH, '//*[@id="navbarMenu"]/ul/li[2]/ul/li[4]/a')
    stripwich_dropdown_btn = (By.XPATH, '//*[@id="navbarMenu"]/ul/li[2]/ul/li[5]/a')
    calzone_dropdown_btn = (By.XPATH, '//*[@id="navbarMenu"]/ul/li[2]/ul/li[6]/a')
    chicken_dropdown_btn = (By.XPATH, '//*[@id="navbarMenu"]/ul/li[2]/ul/li[7]/a')
    sides_dropdown_btn = (By.XPATH, '//*[@id="navbarMenu"]/ul/li[2]/ul/li[8]/a')
    salads_dropdown_btn = (By.XPATH, '//*[@id="navbarMenu"]/ul/li[2]/ul/li[9]/a')
    pasta_dropdown_btn = (By.XPATH, '//*[@id="navbarMenu"]/ul/li[2]/ul/li[10]/a')
    deserts_dropdown_btn = (By.XPATH, '//*[@id="navbarMenu"]/ul/li[2]/ul/li[11]/a')
    drinks_dropdown_btn = (By.XPATH, '//*[@id="navbarMenu"]/ul/li[2]/ul/li[12]/a')
    sausage_dropdown_btn = (By.XPATH, '//*[@id="navbarMenu"]/ul/li[2]/ul/li[13]/a')
    menus_dropdown_btn = (By.XPATH, '//*[@id="navbarMenu"]/ul/li[2]/ul/li[14]/a')

    about_campaigns_dropdown_btn = (By.XPATH, "(//a[normalize-space()='Campanii'])[1]")
    about_jobs_dropdown_btn = (By.XPATH, "(//a[@role='button'][normalize-space()='Joburi'])[1]")
    about_products_dropdown_btn = (By.XPATH, "(//a[normalize-space()='Produse'])[1]")
    about_news_dropdown_btn = (By.XPATH, "(//a[normalize-space()='Noutati'])[1]")
    about_quantities_dropdown_btn = (By.XPATH, '//ul[contains(@class,"dropdown-menu p-0 border-0 shadow show")]//li[5]')
    about_contact_dropdown_btn = (By.XPATH, "(//a[@role='button'][normalize-space()='Contact'])[1]")

    my_account_btn = (By.ID, "myAccountDropdown")
    success_logged_in_mssg = (By.XPATH, '/html/body/div/div[1]/div/div/div[1]/div[2]')
    invalid_mail_message = (By.XPATH, '/html/body/div/div[2]/div/div/div/div[2]/div[2]/p')
    invalid_pwd_or_mail_message = (By.XPATH, "//p[@id='outlined-weight-helper-text']")
    enter_acc_btn1 = (By.CSS_SELECTOR, "#navbarMenu > div > ul > li.nav-item.dropdown > ul > li:nth-child(2) > div > button.btn.btn-sm.btn-primary")
    input_saved_mail = (By.ID, 'mui-1')
    input_saved_pwd = (By.ID, 'outlined-adornment-password')
    enter_acc_btn2 = (By.ID, 'mui-2')
    new_account_btn = (By.CSS_SELECTOR, "#navbarMenu > div > ul > li.nav-item.dropdown > ul > li:nth-child(2) > div > button.btn.btn-sm.text-info")
    input_mail = (By.ID, 'mui-3')
    input_phone_number = (By.ID, 'mui-4')
    input_name = (By.XPATH, "//input[@type='text' and contains(@class, 'MuiInputBase-input') and contains(@class, 'MuiOutlinedInput-input') and contains(@class, 'css-1x5jdmq')]")
    pwd_inputs = (By.XPATH, "//input[@type='password' and contains(@class, 'MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputAdornedEnd css-1uvydh2')]")

    create_acc_btn = (By.XPATH, '//button[normalize-space()="Cont nou"]')
    create_acc_final_btn = (By.XPATH, '//*[@id="mui-5"]')
    no_offers_to_receive_button_pop_up = (By.XPATH, "//button[@type='button' and contains(@class, 'MuiButtonBase-root MuiButton-root MuiButton-text MuiButton-textPrimary MuiButton-sizeMedium MuiButton-textSizeMedium MuiButton-root MuiButton-text MuiButton-textPrimary MuiButton-sizeMedium MuiButton-textSizeMedium css-tjm7sl')][1]")
    confirmation_sms_pop_up = (By.XPATH, "/html/body/div[4]/div/div/div[1]/h3")

    calzone_homepg_btn = (By.XPATH, '//a[@href="/produse/Calzone"]')
    salads_homepg_btn = (By.XPATH, '//a[@href="/produse/Salate"]')
    desert_homepg_btn = (By.XPATH, '//a[@href="/produse/Desert"]')
    drinks_homepg_btn = (By.XPATH, '//a[@href="/produse/Bauturi"]')
    sausages_homepg_btn = (By.XPATH, '//a[@href="/produse/Sos"]')

    terms_conditions_btn = (By.XPATH, '//*[@id="__next"]/div[2]/footer/div[2]/div/div[2]/div/ul/li[1]/a')
    confidentiality_policy_btn = (By.PARTIAL_LINK_TEXT, "confidentialitate")
    loyalty_policy_btn = (By.PARTIAL_LINK_TEXT, "loialitate")
    night_schedule_program_btn = (By.XPATH, '//*[@id="__next"]/div[2]/footer/div[2]/div/div[3]/div/ul/li[3]/label[1]/a')
    night_schedule_box_info = (By.XPATH, '//p[contains(text(),"Pentru comenzile cu valoare mai mica de 60 lei liv")]')

    accept_cookie_btn = (By.ID, 'CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll')
    facebook_page_btn = (By.XPATH, '//a[@class="fs-4 text-info"]')

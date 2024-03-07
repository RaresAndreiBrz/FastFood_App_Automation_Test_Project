
from selenium.webdriver.common.by import By



class JobsPageLocators:

    delivery_job_section = (By.ID, "nav-1-tab")
    cooking_job_section = (By.ID, "nav-2-tab")
    shift_manager_section = (By.ID, "nav-3-tab")
    unit_manager_section = (By.ID, "nav-4-tab")
    calls_operator_section = (By.ID, "nav-5-tab")

    name_input = (By.XPATH, '//input[@id="mui-1"]')
    phone_number_input = (By.XPATH, '//label[@id="mui-2-label"]')
    mail_input = (By.XPATH, '//input[@id="mui-3"]')

    delivery_btn_input = (By.XPATH, '//*[@id="__next"]/div[2]/div/div/div[2]/div/div[2]/div/div[4]/ul/div[1]/div[1]')
    delivery_with_personal_car_btn_input = (By.XPATH, '//body/div[@id="__next"]/div[@class="d-flex flex-column h-100"]/div[@class="container bg-white p-4 shadow rounded-top"]/div[@class="row"]/div[@class="col-12 col-lg-4"]/div[@class="card"]/div[@class="card-body"]/div[@class="d-flex flex-column"]/div/ul[@class="MuiList-root MuiList-padding css-1mmpiy9"]/div/div/div[@class="MuiCollapse-root MuiCollapse-vertical MuiCollapse-entered css-c4sutr"]/div[@class="MuiCollapse-wrapper MuiCollapse-vertical css-hboir5"]/div[@class="MuiCollapse-wrapperInner MuiCollapse-vertical css-8atqhb"]/div[@class="MuiList-root css-1iero1v"]/li[1]/div[1]')
    delivery_with_company_car_btn_input = (By.XPATH, '//body/div[@id="__next"]/div[@class="d-flex flex-column h-100"]/div[@class="container bg-white p-4 shadow rounded-top"]/div[@class="row"]/div[@class="col-12 col-lg-4"]/div[@class="card"]/div[@class="card-body"]/div[@class="d-flex flex-column"]/div/ul[@class="MuiList-root MuiList-padding css-1mmpiy9"]/div/div/div[@class="MuiCollapse-root MuiCollapse-vertical MuiCollapse-entered css-c4sutr"]/div[@class="MuiCollapse-wrapper MuiCollapse-vertical css-hboir5"]/div[@class="MuiCollapse-wrapperInner MuiCollapse-vertical css-8atqhb"]/div[@class="MuiList-root css-1iero1v"]/li[2]/div[1]')
    cooking_btn_input = (By.XPATH, '//*[@id="__next"]/div[2]/div/div/div[2]/div/div[2]/div/div[4]/ul/div[2]/div[1]')
    shift_manager_input = (By.XPATH, '//*[@id="__next"]/div[2]/div/div/div[2]/div/div[2]/div/div[4]/ul/div[3]/div[1]')
    unit_manager_input = (By.XPATH, '//*[@id="__next"]/div[2]/div/div/div[2]/div/div[2]/div/div[4]/ul/div[4]/div[1]')
    calls_operator_input = (By.XPATH, '//*[@id="__next"]/div[2]/div/div/div[2]/div/div[2]/div/div[4]/ul/div[5]/div[1]')
    select_city_Bucharest_input = (By.XPATH, '//body/div[@id="__next"]/div[@class="d-flex flex-column h-100"]/div[@class="container bg-white p-4 shadow rounded-top"]/div[@class="row"]/div[@class="col-12 col-lg-4"]/div[@class="card"]/div[@class="card-body"]/div[@class="d-flex flex-column"]/div/nav[@class="MuiList-root MuiList-padding css-16t2dxn"]/div[1]')
    select_Sector6_Bucharest_input = (By.XPATH, '//nav[@class="MuiList-root MuiList-padding css-16t2dxn"]//li[1]')
    agree_with_terms_input = (By.XPATH, '//input[@aria-label="controlled"]')
    send_application_btn = (By.XPATH, '//button[@id="mui-4"]')

    delivery_informations_box = (By.XPATH, '//div[@id="nav-1"]//ul')
    cooking_informations_box = (By.XPATH, '//div[@id="nav-2"]')
    shift_manager_informations_box = (By.XPATH, '//div[@id="nav-3"]')
    unit_manager_informations_box = (By.XPATH, '//div[@id="nav-4"]')
    calls_operator_informations_box = (By.XPATH, '//div[@id="nav-5"]')

    confirmation_message_box = (By.XPATH, '//p[@class="MuiTypography-root MuiTypography-body1 css-122eukp"]')

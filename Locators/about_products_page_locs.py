from selenium.webdriver.common.by import By


class AboutProductsPageLocators:

    title_of_the_page = (By.XPATH, '//h1[normalize-space()="Despre produse"]')

    pizza_title = (By.XPATH, '//h3[normalize-space()="Despre Pizza"]')
    pizza_text = (By.XPATH, "(//div[@class='col-md-9'])[1]")
    calzone_title = (By.XPATH, '//h3[normalize-space()="Despre Calzone"]')
    calzone_text = (By.XPATH, "(//div[@class='col-md-9'])[2]")
    stripwich_title = (By.XPATH, '//h3[normalize-space()="Despre Stripwich"]')
    stripwich_text = (By.XPATH, "(//div[@class='col-md-9'])[3]")
    bbq_title = (By.XPATH, '//h3[normalize-space()="Despre BBQ Wings"]')
    bbq_text = (By.XPATH, "(//div[@class='col-md-9'])[4]")
    pasta_title = (By.XPATH, '//h3[normalize-space()="Despre Paste"]')
    pasta_text = (By.XPATH, "(//div[@class='col-md-9'])[5]")

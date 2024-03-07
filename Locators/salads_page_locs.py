
from selenium.webdriver.common.by import By



class SaladsPageLocators:

    products_listed_on_page = (By.XPATH, "(//div[@class='col'])")

    salad_Veggie_btn = (By.XPATH, "//body[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/a[1]")
    salad_Caesar_btn = (By.XPATH, "//body[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[3]/button[1]")
    salad_Home_btn = (By.XPATH, "//body[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/a[1]")
    salad_Tuna_btn = (By.XPATH, "//body[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[5]/div[1]/div[1]/a[1]")
    informations_boxes1 = (By.XPATH, "//body[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]")
    informations_boxes2 = (By.XPATH, "//body[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]")
    informations_boxes3 = (By.XPATH, "//body[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[3]/div[1]/div[2]")
    informations_boxes4 = (By.XPATH, "//body[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[4]/div[1]/div[2]")
    informations_boxes5 = (By.XPATH, "//body[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[5]/div[1]/div[2]")
    informations_boxes6 = (By.XPATH, "//body[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[6]/div[1]/div[2]")
    info_button_of_Mediterana_salad = (By.XPATH, '//a[@href="/produse/Salate?name=Salata+Mediterana&gramaje=true"]//button[@type="button"]//*[name()="svg"]')
    ingredients_btn_of_Medit_salad = (By.XPATH, '//div[@class="d-none d-md-block"]//button[@id="simple-tab-0"]')


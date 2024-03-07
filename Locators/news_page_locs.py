
from selenium.webdriver.common.by import By



class NewsPageLocators:


    dates_of_all_news = (By.XPATH, '//span[@class="text-primary"]')
    news_imgs = (By.XPATH, '//body[1]/div[1]/div[2]/div[1]/div[1]/div/div[1]/div[1]/img[1]')
    news_titles = (By.XPATH, 'text-center mb-3 text-info mb-4')

    news_1_box = (By.XPATH, "(//div[@class='col'])[1]")
    news_1_box_title = (By.XPATH, '//h5[contains(text(),"Cluj-N")]')
    news1_title_inside = (By.XPATH, '//h1[contains(text(),"Cluj-N")]')

    date_of_the_news3 = (By.XPATH, '//span[@class="text-primary"][3]')
    news_3_introduction = (By.XPATH, '//p[contains(text(),"Calea Bucureș")]')

    news_5_box = (By.XPATH, "(//a[contains(text(),'Detalii')])[5]")
    story_of_the_news5 = (By.XPATH, "(//strong[contains(text(),'General Manager')])[1]")
    news_5_img = (By.XPATH, '//body[1]/div[1]/div[2]/div[1]/div[1]/div[5]/div[1]/div[1]/img[1]')

    news_7_box = (By.XPATH, '//h5[contains(text(),"Balotesti")]')
    news7_newspage_date = (By.XPATH, '//span[normalize-space()="10 Dec 2019, 11:55"]')
    news7_date = (By.XPATH, '//span[normalize-space()="10 Dec 2019, 11:55"]')

    news_9_box = (By.XPATH, '//body/div[@id="__next"]/div[@class="d-flex flex-column h-100"]/div[@class="container"]/div[@class="row row-cols-1 row-cols-md-2 row-cols-lg-2 row-cols-xl-3 g-2 mb-5"]/div[9]')

    first_img = (By.XPATH, '//img[@alt="71149756_10157646102002767_7935333124563533824_o"]')





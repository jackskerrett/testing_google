from selenium.webdriver.common.by import By


class Homepage:
    url = 'https://www.google.com/'
    close_pop_up_button = (By.ID, 'L2AGLb')
    sign_in_button = (By.XPATH, "/html/body/div[1]/div[1]/div/div/div/div[2]/a")
    pop_up_on_initial_load = (By.ID, 'CXQnmb')
    user_icon = (By.XPATH, '//*[@id="gb"]/div/div[2]/div[2]/div/a')

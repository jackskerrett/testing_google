from selenium.webdriver.common.by import By


class SignIn:
    email_input_box = (By.ID, "identifierId")
    email_page_next_button = (By.XPATH, '//*[@id="identifierNext"]/div/button')
    password_input_box = (By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')
    password_page_next_button = (By.XPATH, '//*[@id="passwordNext"]/div/button')

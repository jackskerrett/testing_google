def enter_value(webdriver, element, value):
    webdriver.find_element(*element).clear()
    webdriver.find_element(*element).send_keys(value)
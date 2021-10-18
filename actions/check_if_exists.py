def check_if_exists(webdriver, element):
    return webdriver.find_element(*element)
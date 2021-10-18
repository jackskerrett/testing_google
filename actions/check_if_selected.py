def check_if_selected(webdriver, element):
    return webdriver.find_element(*element).is_selected()
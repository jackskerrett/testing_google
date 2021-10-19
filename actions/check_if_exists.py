from selenium.common.exceptions import NoSuchElementException       

def check_if_exists(webdriver, element):
    try:
        webdriver.find_element(*element)
    except NoSuchElementException:
        return False
    return True
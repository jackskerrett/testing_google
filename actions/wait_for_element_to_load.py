from selenium.common.exceptions import NoSuchElementException

def wait_for_element_to_load(webdriver, element):
    while(1):
        try:
            webdriver.find_element(*element)
            break
        except NoSuchElementException:
            continue
    
from selenium.common.exceptions import NoSuchElementException

def wait_for_element_to_load(context, element):
    while(1):
        try:
            context.webdriver.find_element(*element)
            break
        except NoSuchElementException:
            continue
    
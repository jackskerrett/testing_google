from selenium.common.exceptions import NoSuchElementException


def check_if_exists(context, element):
    try:
        context.webdriver.find_element(*element)
    except NoSuchElementException:
        return False
    return True

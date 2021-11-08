from selenium.common.exceptions import ElementClickInterceptedException, ElementNotInteractableException

def wait_for_element_to_be_clickable(context, element):
    while(1):
        try:
            context.webdriver.find_element(*element).click()
            break
        except (ElementClickInterceptedException, ElementNotInteractableException) as e:
            continue
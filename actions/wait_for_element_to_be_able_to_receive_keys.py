from selenium.common.exceptions import ElementNotInteractableException

def wait_for_element_to_be_able_to_receive_keys(context, element):
    while(1):
        try:
            context.webdriver.find_element(*element).send_keys("test")
            context.webdriver.find_element(*element).clear()
            break
        except ElementNotInteractableException:
            continue
from selenium.common.exceptions import InvalidElementStateException

def wait_for_element_to_be_enabled(context, element):
    while(1):
        if(context.webdriver.find_element(*element).is_enabled()):
            while(1):
                try:
                    context.webdriver.find_element(*element).send_keys("1")
                    break
                except InvalidElementStateException:
                    continue
            break
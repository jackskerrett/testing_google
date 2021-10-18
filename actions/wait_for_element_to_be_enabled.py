from selenium.common.exceptions import InvalidElementStateException

def wait_for_element_to_be_enabled(webdriver, element):
    while(1):
        if(webdriver.find_element(*element).is_enabled()):
            while(1):
                try:
                    webdriver.find_element(*element).send_keys("1")
                    break
                except InvalidElementStateException:
                    continue
            break

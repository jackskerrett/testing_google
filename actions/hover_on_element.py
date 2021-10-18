from selenium.webdriver.common.action_chains import ActionChains

def hover_on_element(webdriver, element):
    action = ActionChains(webdriver)
    action.move_to_element(webdriver.find_element(*element)).perform()

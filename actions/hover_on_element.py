from selenium.webdriver.common.action_chains import ActionChains

def hover_on_element(context, element):
    action = ActionChains(context.webdriver)
    action.move_to_element(context.webdriver.find_element(*element)).perform()

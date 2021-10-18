def get_tool_tip_value(webdriver, element):
    return webdriver.find_element(*element).text
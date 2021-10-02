def get_tool_tip_value(context, element):
    return context.webdriver.find_element(*element).text
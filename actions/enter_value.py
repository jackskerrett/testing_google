def enter_value(context, element, value):
    context.webdriver.find_element(*element).clear()
    context.webdriver.find_element(*element).send_keys(value)
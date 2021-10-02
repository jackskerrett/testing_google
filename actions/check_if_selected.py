def check_if_selected(context, element):
    return context.webdriver.find_element(*element).is_selected()
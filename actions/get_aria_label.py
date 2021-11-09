def get_aria_label(context, element):
    return context.webdriver.find_element(*element).get_attribute("aria-label")

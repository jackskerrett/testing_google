def click_on(context, element):
    context.webdriver.find_element(*element).click()
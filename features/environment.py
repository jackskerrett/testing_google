from selenium import webdriver

def before_scenario(context, scenario):
    context.webdriver = webdriver.Chrome(executable_path="testing_google/chromedriver.exe")

def after_scenario(context, scenario):
    context.webdriver.close()

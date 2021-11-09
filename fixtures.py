from pytest import fixture
from selenium import webdriver
from users.default_user import DefaultUser

class Context:
    pass

@fixture
def default_browser():
    context = Context()
    browser_options = webdriver.FirefoxOptions()
    browser_options.headless = True
    context.webdriver = webdriver.Firefox(options = browser_options)
    context.actor = DefaultUser
    yield context
    context.webdriver.quit()
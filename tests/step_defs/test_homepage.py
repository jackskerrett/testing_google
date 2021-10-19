from pytest import fixture
from selenium import webdriver
from pytest_bdd import scenarios, given, when, then
from pages.homepage import Homepage
from actions.check_if_exists import check_if_exists
from tasks.load_google_home_page import load_google_home_page

scenarios('../../features/homepage.feature')

@fixture
def browser():
    browser_options = webdriver.FirefoxOptions()
    browser_options.headless = True
    b = webdriver.Firefox(options = browser_options)
    yield b
    b.quit()

@given('the Google home page is loaded')
def google_home(browser):
    load_google_home_page(browser)



@then('there is an option to sign in')
def check_login_option(browser):
    assert(check_if_exists(browser, Homepage.sign_in_button))
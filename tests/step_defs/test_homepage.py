from pytest import fixture
from selenium import webdriver
from pytest_bdd import scenarios, given, when, then
from pages.homepage import Homepage
from actions.navigate_to import navigate_to
from actions.click_on import click_on
from actions.check_if_exists import check_if_exists
from sys import argv

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
    navigate_to(browser, Homepage.url)
    click_on(browser, Homepage.close_pop_up_button)


@then('there is an option to sign in')
def check_login_option(browser):
    assert(check_if_exists(browser, Homepage.sign_in_button) != None)
from pytest_bdd import scenarios, given, when, then
from fixtures import default_browser
from tasks.load_google_home_page import load_google_home_page
from tasks.click_sign_in_button import click_sign_in_button
from tasks.enter_email_address_for_login import enter_email_address_for_login
from tasks.enter_password_for_login import enter_password_for_login
from tasks.get_logged_in_user import get_logged_in_user

scenarios('../../features/login.feature')

@given('the Google homepage is displayed')
def the_google_homepage_is_displayed(default_browser):
    load_google_home_page(default_browser)


@when('the sign in button is pressed')
def the_sign_in_button_is_pressed(default_browser):
    click_sign_in_button(default_browser)


@when('valid user credentials are entered')
def valid_user_credentials_are_entered(default_browser):
    enter_email_address_for_login(default_browser)
    enter_password_for_login(default_browser)

@then('the Google homepage is displayed')
def the_Google_homepage_is_displayed(default_browser):
    pass

@then('an icon in the top right displays the logged in user')
def an_icon_in_the_top_right_displays_the_logged_in_user(default_browser):
    assert(get_logged_in_user(default_browser).split("(")[1].replace(")", "") == default_browser.actor.email_address)


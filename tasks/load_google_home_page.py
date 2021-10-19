from actions.navigate_to import navigate_to
from actions.check_if_exists import check_if_exists
from actions.click_on import click_on
from pages.homepage import Homepage


def load_google_home_page(browser):
    navigate_to(browser, Homepage.url)
    if(check_if_exists(browser, Homepage.pop_up_on_initial_load)):
        click_on(browser, Homepage.close_pop_up_button)
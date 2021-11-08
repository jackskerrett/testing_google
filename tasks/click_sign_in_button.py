from actions.click_on import click_on
from actions.navigate_to import navigate_to
from pages.homepage import Homepage

def click_sign_in_button(context):
    navigate_to(context, Homepage.url)
    click_on(context, Homepage.sign_in_button)



from actions.enter_value import enter_value
from actions.click_on import click_on
from actions.wait_for_element_to_load import wait_for_element_to_load
from pages.sign_in import SignIn


def enter_email_address_for_login(context):
    wait_for_element_to_load(context, SignIn.email_input_box)
    enter_value(context, SignIn.email_input_box, context.actor.email_address)
    click_on(context, SignIn.email_page_next_button)

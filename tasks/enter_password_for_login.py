from actions.enter_value import enter_value
from actions.click_on import click_on
from actions.wait_for_element_to_be_able_to_receive_keys import wait_for_element_to_be_able_to_receive_keys
from actions.wait_for_element_to_load import wait_for_element_to_load
from actions.wait_for_element_to_be_clickable import wait_for_element_to_be_clickable
from pages.sign_in import SignIn

def enter_password_for_login(context):
    wait_for_element_to_load(context, SignIn.password_input_box)
    wait_for_element_to_be_clickable(context, SignIn.password_page_next_button)
    enter_value(context, SignIn.password_input_box, context.actor.password)
    click_on(context, SignIn.password_page_next_button)


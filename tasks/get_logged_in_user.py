from actions.navigate_to import navigate_to
from actions.get_aria_label import get_aria_label
from actions.wait_for_element_to_load import wait_for_element_to_load
from pages.homepage import Homepage

def get_logged_in_user(context):
    navigate_to(context, Homepage.url)
    wait_for_element_to_load(context, Homepage.user_icon)
    return get_aria_label(context, Homepage.user_icon)


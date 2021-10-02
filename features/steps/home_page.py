from behave import given, when, then
from actions.navigate_to import navigate_to
from actions.is_element_present import is_element_present
from pages.home_page import GoogleHomePage

@given(u'a user loads "{webpage}"')
def step_impl(context, webpage):
    navigate_to(context, webpage)


@then(u'there is a sign in button on the page')
def step_impl(context):
   is_element_present(context, GoogleHomePage.sign_in_button)
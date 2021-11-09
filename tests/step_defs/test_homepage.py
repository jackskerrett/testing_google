# from fixtures import default_browser
# from pytest_bdd import scenarios, given, when, then
# from pages.homepage import Homepage
# from actions.check_if_exists import check_if_exists
# from tasks.load_google_home_page import load_google_home_page

# scenarios('../../features/homepage.feature')



# @given('the Google home page is loaded')
# def google_home(default_browser):
#     load_google_home_page(default_browser)

# @then('there is an option to sign in')
# def check_login_option(default_browser):
#     assert(check_if_exists(default_browser, Homepage.sign_in_button))
from nose.tools import assert_equal, assert_true
from selenium.webdriver.common.by import By

@step('I click Profile')
def step_impl(context):
    context.home_page.popprofile()

@step('I click Logout')
def step_impl(context):
    context.home_page.logout()

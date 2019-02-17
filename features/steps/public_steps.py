from nose.tools import assert_equal, assert_true
from selenium.webdriver.common.by import By

@step('I waiting for "{time}" seconds')
def step_impl(context, time):
    context.home_page.waiting(time)

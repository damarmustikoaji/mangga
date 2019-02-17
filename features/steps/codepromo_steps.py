from nose.tools import assert_equal, assert_true
from selenium.webdriver.common.by import By

@step('I see the Promo Share Modal')
def step_impl(context):
    context.home_page.promoshare_modal()

@step('I click Close Promo')
def step_impl(context):
    context.home_page.close()

from nose.tools import assert_equal, assert_true
from selenium.webdriver.common.by import By

@step('I click Test')
def step_impl(context):
    context.public_page.test()

@step('I waiting for "{time}" seconds')
def step_impl(context, time):
    context.home_page.waiting(time)

@step('I click text "{text}"')
def step_impl(context, text):
    context.home_page.click_text(text)

@step('I assert the maintenance info "{text}"')
def step_impl(context, text):
    assert_equal(context.home_page.get_element(), "Ralali Wallet is currently down for maintenance. We expect to be back in a couple hours. Thanks for your patience. See Ralali Wallet")
    content.home_page.closemaintenance()

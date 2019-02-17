from nose.tools import assert_equal, assert_true
from selenium.webdriver.common.by import By
from behave import given, then, when

@step('I click Login')
def step_impl(context):
    context.home_page.login()

@step('I fill email field using "{EMAIL}"')
def step_impl(context, EMAIL):
    context.home_page.emailfill(EMAIL)

@step('I fill password field using "{PASSWORD}"')
def step_impl(context, PASSWORD):
    context.home_page.passwordfill(PASSWORD)

@step('I see a home page "{text}"')
def step_impl(context, text):
    assert_true(context.home_page.verify(text))

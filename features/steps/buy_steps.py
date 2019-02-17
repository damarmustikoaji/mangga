from nose.tools import assert_equal, assert_true
from selenium.webdriver.common.by import By

@step('I buy product "{product}"')
def step_impl(context, product):
    context.home_page.buy(product)

@step('I see the Shopping Cart')
def step_impl(context):
    context.home_page.shopping_cart()

@step('I click Checkout')
def step_impl(context):
    context.home_page.checkout()

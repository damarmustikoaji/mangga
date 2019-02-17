from nose.tools import assert_equal, assert_true
from selenium.webdriver.common.by import By

@step('I see the Wallet Activation')
def step_impl(context):
    context.home_page.walletmodal()

@step('I click "{confirm}" for Wallet Activation')
def step_impl(context, confirm):
    context.home_page.walletactivation(confirm)

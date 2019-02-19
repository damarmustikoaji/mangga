from nose.tools import assert_equal, assert_true
from selenium.webdriver.common.by import By

@step('I navigate to "{URL}"')
def step_impl(context, URL):
    context.home_page.navigate(URL)

@step('I see a the title Ralali.com page')
def step_impl(context, URL):
    assert_equal(context.home_page.get_page_title(), "B2B Marketplace Indonesia - Harga Grosir dari Ribuan Penjual | Ralali.com")

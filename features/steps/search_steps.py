from nose.tools import assert_equal, assert_true
from selenium.webdriver.common.by import By

@step('I search for "{search_term}"')
def step_impl(context, search_term):
    context.home_page.search(search_term)

@step('I am taken to the "{search_term}" Search Results page')
def step_impl(context, search_term):
    assert_equal(context.search_results_page.get_page_title(), "Harga Grosir "+search_term+" Terbaru Februari 2019 | Ralali.com")

@step('I see a search result "{search_result}"')
def step_impl(context, search_result):
    assert_true(context.search_results_page.find_search_result(search_result))

from nose.tools import assert_equal, assert_true
from selenium.webdriver.common.by import By

@step('I click Buy')
def step_impl(context):
    context.product_page.Buy()

@step('I see the Shopping Cart')
def step_impl(context):
    context.product_page.ShoppingCart()

@step('I click Checkout')
def step_impl(context):
    context.product_page.CheckOut()

@step('I click Continue with shipping')
def step_impl(context):
    context.product_page.ContinueWithShipping()

@step('I choose Shipping with "{ex}" and type "{type}"')
def step_impl(context, ex, type):
    context.product_page.Shippingwith(ex, type)

@step('I click Continue with payment')
def step_impl(context):
    context.product_page.continuewithpayment()

@step('I choose payment method using "{method}')
def step_impl(context, method):
    context.product_page.ContinueWithPayment(method)

@step('I click Place order and pay')
def step_impl(context):
    context.home_page.placeorderandpay()

@step('I fill number Credit Card')
def step_impl(context):
    context.product_page.CreditCard()

@step('I fill number OVO')
def step_impl(context):
    context.product_page.OVO()

@step('I click Continue to checkout')
def step_impl(context):
    context.product_page.ContinueToCheckout()

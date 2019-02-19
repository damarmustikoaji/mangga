import time
from selenium.webdriver.common.by import By
from browser import Browser
from selenium.webdriver.common.action_chains import ActionChains

from pages.object_repository import ObjectRepository
from pages.public_library import PublicLibrary

class ProductPage(Browser):
    # Public Page Actions

    def Buy(self):
        obj     = ObjectRepository
        func    = PublicLibrary
        try:
            func.click_element(self, *obj.BUY_BTN)
        except Exception as e:
            func.click_element(self, *obj.BUY_BTN2)

    def ShoppingCart(self):
        obj     = ObjectRepository
        func    = PublicLibrary
        func.get_element(self, *obj.SHOP_CART)

    def CheckOut(self):
        obj     = ObjectRepository
        func    = PublicLibrary
        func.click_element(self, *obj.CHECKOUT_BTN)

    def ContinueWithShipping(self):
        obj     = ObjectRepository
        func    = PublicLibrary
        func.click_element(self, *obj.SHIPPING_BTN)

    def Shippingwith(self, ex, type):
        obj     = ObjectRepository
        func    = PublicLibrary
        time.sleep(3)
        func.get_text_element(self, *obj.SHIPWITH_BTN)

    def ContinueWithPayment(self, method):
        obj     = ObjectRepository
        func    = PublicLibrary
        func.click_element(self, *obj.CONTINUE_PAYMENT)
        if "Credit Card" in method:
            func.click_element(self, *obj.CREDIT_CARD)
        elif "OVO" in method:
            func.click_element(self, *obj.OVO)
        func.click_element(self, *obj.PAY_BTN)

    def CreditCard(self):
        obj     = ObjectRepository
        func    = PublicLibrary
        func.get_element(self, *obj.CC_MODAL)
        time.sleep(1)
        func.click_element(self, *obj.CONTINUE_BTN)
        time.sleep(3)
        func.click_element(self, *obj.PAYNOW_BTN)

    def OVO(self):
        obj     = ObjectRepository
        func    = PublicLibrary
        func.fill(self, "12345678", *obj.OVO_MODAL)
        func.click_element(self, *obj.OVO_OK)

    def ContinueToCheckout(self):
        obj     = ObjectRepository
        func    = PublicLibrary
        func.click_element(self, *obj.CONTINUE_CHECKOUT)

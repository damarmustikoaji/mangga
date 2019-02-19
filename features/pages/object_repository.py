import time
from selenium.webdriver.common.by import By

class ObjectRepository(object):
    # Object Repository Locators

    HEADER_TEXT     = (By.XPATH, '//h1')

    SEARCH_FIELD    = (By.NAME, 'search')
    SUBMIT_BUTTON   = (By.XPATH, '//button[@class="btn btnSearchHome" and @type="submit"]')

    LOGIN_BUTTON    = (By.XPATH, '//a[@class="btnHomeLogin btn btn-primary-ghost btn-alt btn-wide"]')
    EMAIL_FIELD     = (By.NAME, 'email')
    NEXT_BUTTON     = (By.XPATH, '//button[@class="btn btn-primary pull-right" and @type="submit"]')
    PASSWORD_FIELD  = (By.NAME, 'password')
    LOGIN_BUTTON2   = (By.XPATH, '//button[@class="btnHomeLogin btn btn-primary" and @type="button"]')

    ERROR_MSG       = (By.XPATH, '//div[@class="text-danger ng-binding ng-scope"]')

    PROFILE         = (By.XPATH, '//span[@class="account-header-greeting"]')
    POPUP_PROFILE   = (By.XPATH, '//div[@class="popover ng-isolate-scope bottom popover-profile fade in"]')
    LOGOUT          = (By.XPATH, '//i[@class="fa fa-ralali-logout"]')

    WALLET_MODAL    = (By.XPATH, '//div[@class="modal-content modal-primary"]')
    LATER_BUTTON    = (By.XPATH, '//a[@class="btn btn-primary-ghost btn-fixed wallet-actp1-later"]')
    ACTIVATE_BUTTON = (By.XPATH, '//a[@class="btn btn-primary btn-fixed wallet-actp1-activate"]')
    CLOSE_BUTTON    = (By.XPATH, '//div[@class="feedback-close"]')

    #Buying
    BUY_BTN         = (By.ID, 'btn-add-to-cart')
    BUY_BTN2        = (By.XPATH, '//button[@class="btn btn-primary btn-block btn-beli-special hidden-xs hidden-sm ng-binding ng-scope"]')
    SHOP_CART       = (By.XPATH, '//tr[@data-ng-init="ctrl.calculation()" and @data-ng-repeat-start="(k, v) in value"]')
    CHECKOUT_BTN    = (By.XPATH, '//button[@type="button" and @class="btn btn-secondary ng-binding"]')
    SHIPPING_BTN    = (By.ID, 'btn-checkout-step-2-shipping')
    SHIPWITH_BTN    = (By.ID, 'shipment-list')
    JNT             = (By.LINK_TEXT, 'J&T')
    EZ              = (By.LINK_TEXT, 'EZ')
    PAYMENT_BTN     = (By.ID, 'btn-checkout-step-3-payment')
    CREDIT_CARD     = (By.XPATH, '//strong[@class="ng-binding" and contains(text(), "Credit Card ")]')
    OVO             = (By.XPATH, '//strong[@class="ng-binding" and contains(text(), "OVO ")]')
    OVO_MODAL       = (By.ID, 'ovo_phone')
    OVO_OK          = (By.XPATH, '//button[@class="btn btn-primary btn-fixed" and @ng-click="shipment.processOvo()"]')
    PAY_BTN         = (By.ID, 'btn-checkout-step-4-confirm-order')
    CC_MODAL        = (By.XPATH, '//div[@class="container-fluid"]')
    CONTINUE_BTN    = (By.XPATH, '//div[@class="pop-wrapper has-close"]')
    PAYNOW_BTN      = (By.XPATH, '//div[@class="pop-wrapper has-close"]/span[@class="pop"]')

    BUY_DETAIL_BUTTON  = (By.ID, 'btn-add-to-cart')
    CART_MODAL      = (By.XPATH, '//div[@class="modal-content res-modal-content-overlay"]')
    CHECKOUT_BUTTON = (By.XPATH, '//button[@id="finishedshopping"]')
    SHIPPING_BUTTON = (By.XPATH, '//button[@class="btn btn-block btn-primary ng-scope" and @id="btn-checkout-step-2-shipping"]')
    SHIPMENT        = (By.ID, 'shipment-list')
    CONTINUE_PAYMENT= (By.XPATH, '//button[@id="btn-checkout-step-3-payment"]')
    CONTINUE_CHECKOUT = (By.ID, 'btn-cart-show-all-initiate-checkout')

    PLACEORDER_ANDPAY= (By.XPATH, '//button[@id="btn-checkout-step-4-confirm-order" and @class="btn btn-block btn-primary ng-scope"]')
    TEL             = (By.XPATH, '//input[@type="tel"]')
    CARDNUMBER      = (By.XPATH, '//input[@name="cardnumber"]')
    EXPIRY          = (By.XPATH, '//input[@type="tel" and @placeholder="MM / YY"]')
    CVV             = (By.XPATH, '//input[@inputmode="numeric" and @placeholder="123"]')
    OK_BUTTON       = (By.XPATH, '//button[@class="btn btn-sm btn-success" and @name="ok"]')

    PROMOSHARE_MODAL= (By.XPATH, '//div[@class="modal-content modal-referral"]')

    CLOSE_MAINTENANCE= (By.XPATH, '//i[@class="multiply icon-close pull-right" and @data-ng-click="home.hideTopBarNotif()"]')

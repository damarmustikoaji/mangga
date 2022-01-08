import time
from selenium.webdriver.common.by import By
from browser import Browser
from selenium.webdriver.common.action_chains import ActionChains

class HomePageLocator(object):
    # Home Page Locators

    HEADER_TEXT     = (By.XPATH, '//h1')

    SEARCH_FIELD    = (By.NAME, 'search')
    SUBMIT_BUTTON   = (By.XPATH, '//button[@class="btn btnSearchHome" and @type="submit"]')

    LOGIN_BUTTON    = (By.XPATH, '//button[@data-testid="button-submit"]')
    EMAIL_FIELD     = (By.ID, 'username')
    NEXT_BUTTON     = (By.XPATH, '//button[@class="btn btn-primary pull-right" and @type="submit"]')
    PASSWORD_FIELD  = (By.XPATH, '//input[@data-testid="input-password"]')
    LOGIN_BUTTON2   = (By.XPATH, '//button[@class="btnHomeLogin btn btn-primary" and @type="button"]')

    ERROR_MSG       = (By.XPATH, '//div[@class="text-danger ng-binding ng-scope"]')

    PROFILE         = (By.XPATH, '//span[@class="account-header-greeting"]')
    POPUP_PROFILE   = (By.XPATH, '//div[@class="popover ng-isolate-scope bottom popover-profile fade in"]')
    LOGOUT          = (By.XPATH, '//i[@class="fa fa-ralali-logout"]')

    WALLET_MODAL    = (By.XPATH, '//div[@class="modal-content modal-primary"]')
    LATER_BUTTON    = (By.XPATH, '//a[@class="btn btn-primary-ghost btn-fixed wallet-actp1-later"]')
    ACTIVATE_BUTTON = (By.XPATH, '//a[@class="btn btn-primary btn-fixed wallet-actp1-activate"]')
    CLOSE_BUTTON    = (By.XPATH, '//div[@class="feedback-close"]')

    BUY_BUTTON      = (By.XPATH, '//button[@class="btn btn-primary btn-block btn-beli-special hidden-xs hidden-sm ng-binding ng-scope"]')
    BUY_DETAIL_BUTTON  = (By.ID, 'btn-add-to-cart')
    CART_MODAL      = (By.XPATH, '//div[@class="modal-content res-modal-content-overlay"]')
    CHECKOUT_BUTTON = (By.XPATH, '//button[@id="finishedshopping"]')
    SHIPPING_BUTTON = (By.XPATH, '//button[@class="btn btn-block btn-primary ng-scope" and @id="btn-checkout-step-2-shipping"]')
    SHIPMENT        = (By.ID, 'shipment-list')
    CONTINUE_PAYMENT= (By.XPATH, '//button[@id="btn-checkout-step-3-payment"]')
    CREDIT_CARD     = (By.XPATH, '//strong[@class="ng-binding" and contains(text(), "Credit Card ")]')
    PLACEORDER_ANDPAY= (By.XPATH, '//button[@id="btn-checkout-step-4-confirm-order" and @class="btn btn-block btn-primary ng-scope"]')
    CONTINUE_BTN     = (By.XPATH, '//div[@class="button-main show"]')
    CONTINUE_BTN2    = (By.XPATH, '//div[@class="button-main show"]')
    TEL             = (By.XPATH, '//input[@type="tel"]')
    CARDNUMBER      = (By.XPATH, '//input[@name="cardnumber"]')
    EXPIRY          = (By.XPATH, '//input[@type="tel" and @placeholder="MM / YY"]')
    CVV             = (By.XPATH, '//input[@inputmode="numeric" and @placeholder="123"]')
    OK_BUTTON       = (By.XPATH, '//button[@class="btn btn-sm btn-success" and @name="ok"]')

    PROMOSHARE_MODAL= (By.XPATH, '//div[@class="modal-content modal-referral"]')

    CLOSE_MAINTENANCE= (By.XPATH, '//i[@class="multiply icon-close pull-right" and @data-ng-click="home.hideTopBarNotif()"]')

class HomePage(Browser):
    # Home Page Actions

    def fill(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def click_element(self, *locator):
        self.driver.find_element(*locator).click()

    def get_element(self, *locator):
        return self.driver.find_element(*locator)

    def scroll_element(self, *locator):
        for i in range(8):
            try:
                if self.get_element(*locator).is_displayed():
                    break
            except: pass
            self.driver.execute_script("window.scrollTo(0, window.scrollY + 200)")
            time.sleep(1)

    def navigate(self, address):
        return self.driver.get(address)

    def get_page_title(self):
        return self.driver.title

    def search(self, search_term):
        self.fill(search_term, *HomePageLocator.SEARCH_FIELD)
        self.click_element(*HomePageLocator.SUBMIT_BUTTON)

    def login(self):
        self.click_element(*HomePageLocator.LOGIN_BUTTON)

    def emailfill(self, email):
        self.fill(email, *HomePageLocator.EMAIL_FIELD)
        # self.click_element(*HomePageLocator.NEXT_BUTTON)

    def passwordfill(self, password):
        self.fill(password, *HomePageLocator.PASSWORD_FIELD)
        # self.click_element(*HomePageLocator.LOGIN_BUTTON2)

    def verify(self, text):
        return self.get_element(By.XPATH, '//*[contains(text(), "'+text+'")]')

    def popprofile(self):
        self.click_element(*HomePageLocator.PROFILE)
        self.get_element(*HomePageLocator.POPUP_PROFILE)
        self.click_element(By.XPATH, '//*[contains(text(), "Logout")]')

    def logout(self):
        self.click_element(By.XPATH, '//*[contains(text(), "Logout")]')

    def walletmodal(self):
        return self.get_element(*HomePageLocator.WALLET_MODAL)

    def walletactivation(self, confirm):
        if confirm == "Activate":
            self.click_element(*HomePageLocator.ACTIVATE_BUTTON)
        else:
            self.click_element(*HomePageLocator.LATER_BUTTON)

    def close(self):
        self.click_element(*HomePageLocator.CLOSE_BUTTON)

    def closemaintenance(self):
        self.click_element(*HomePageLocator.CLOSE_MAINTENANCE)

    def waiting(self, x):
        x = int(x)
        time.sleep(x)

    def buy(self):
        #hover = ActionChains(self.driver).move_to_element(self.get_element(By.XPATH, '//*[contains(text(), "'+product+'")]'))
        #hover.perform()
        self.click_element(*HomePageLocator.BUY_DETAIL_BUTTON)

    def shopping_cart(self):
        #self.get_element(*HomePageLocator.CART_MODAL)
        self.get_element(By.XPATH, '//tr[@data-ng-init="ctrl.calculation()" and @class="ng-scope"]')

    def promoshare_modal(self):
        return self.get_element(*HomePageLocator.PROMOSHARE_MODAL)

    def checkout(self):
        self.get_element(By.XPATH, '//tr[@data-ng-init="ctrl.calculation()" and @class="ng-scope"]')
        self.click_element(*HomePageLocator.CHECKOUT_BUTTON)

    def continuewithshipping(self):
        self.click_element(*HomePageLocator.SHIPPING_BUTTON)

    def shipment(self, ekspedisi, type):
        self.click_element(*HomePageLocator.SHIPMENT)
        self.click_element(By.LINK_TEXT, ekspedisi)
        time.sleep(5)

    def continuewithpayment(self):
        self.click_element(*HomePageLocator.CONTINUE_PAYMENT)

    def creditcard(self):
        self.scroll_element(*HomePageLocator.CREDIT_CARD)
        self.click_element(*HomePageLocator.CREDIT_CARD)

    def placeorderandpay(self):
        self.click_element(*HomePageLocator.PLACEORDER_ANDPAY)

    def fillcc(self, phone, cardnumber, expire, cvv):
        self.click_element(*HomePageLocator.CONTINUE_BTN)
        self.fill(phone, *HomePageLocator.TEL)
        self.fill(cardnumber, *HomePageLocator.CARDNUMBER)
        self.fill(expire, *HomePageLocator.EXPIRY)
        self.fill(cvv, *HomePageLocator.CVV)
        self.click_element(*HomePageLocator.CONTINUE_BTN2)
        self.click_text(*HomePageLocator.OK_BUTTON)

    def click_text(self, text):
        self.scroll_element(By.XPATH, '//*[contains(text(), "'+text+'")]')
        self.click_element(By.XPATH, '//*[contains(text(), "'+text+'")]')
        #self.click_element(By.XPATH, '//*[contains(text(), "'+text+'")]')

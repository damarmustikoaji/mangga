import time
from selenium.webdriver.common.by import By
from browser import Browser
from selenium.webdriver.common.action_chains import ActionChains

class HomePageLocator(object):
    # Home Page Locators

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
    LOGOUT          = (By.XPATH, '//i[@class="fa fa-ralali-logout"]')

    WALLET_MODAL    = (By.XPATH, '//div[@class="modal-content modal-primary"]')
    LATER_BUTTON    = (By.XPATH, '//a[@class="btn btn-primary-ghost btn-fixed wallet-actp1-later"]')
    ACTIVATE_BUTTON = (By.XPATH, '//a[@class="btn btn-primary btn-fixed wallet-actp1-activate"]')
    CLOSE_BUTTON    = (By.XPATH, '//div[@class="feedback-close"]')

    BUY_BUTTON      = (By.XPATH, '//button[@class="btn btn-primary btn-block btn-beli-special hidden-xs hidden-sm ng-binding ng-scope"]')
    CART_MODAL      = (By.XPATH, '//div[@class="modal-content res-modal-content-overlay"]')
    CHECKOUT_BUTTON = (By.XPATH, '//button[@id="finishedshopping" and @class="btn btn-secondary ng-binding"]')

    PROMOSHARE_MODAL= (By.XPATH, '//div[@class="modal-content modal-referral"]')

class HomePage(Browser):
    # Home Page Actions

    def fill(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def click_element(self, *locator):
        self.driver.find_element(*locator).click()

    def get_element(self, *locator):
        return self.driver.find_element(*locator)

    def navigate(self, address):
        self.driver.get(address)

    def get_page_title(self):
        return self.driver.title

    def search(self, search_term):
        self.fill(search_term, *HomePageLocator.SEARCH_FIELD)
        self.click_element(*HomePageLocator.SUBMIT_BUTTON)

    def login(self):
        self.click_element(*HomePageLocator.LOGIN_BUTTON)

    def emailfill(self, email):
        self.fill(email, *HomePageLocator.EMAIL_FIELD)
        self.click_element(*HomePageLocator.NEXT_BUTTON)

    def passwordfill(self, password):
        self.fill(password, *HomePageLocator.PASSWORD_FIELD)
        self.click_element(*HomePageLocator.LOGIN_BUTTON2)

    def verify(self, text):
        return self.get_element(By.XPATH, '//*[contains(text(), "'+text+'")]')

    def popprofile(self):
        self.click_element(*HomePageLocator.PROFILE)

    def logout(self):
        self.click_element(*HomePageLocator.LOGOUT)

    def walletmodal(self):
        return self.get_element(*HomePageLocator.WALLET_MODAL)

    def walletactivation(self, confirm):
        if confirm == "Activate":
            self.click_element(*HomePageLocator.ACTIVATE_BUTTON)
        else:
            self.click_element(*HomePageLocator.LATER_BUTTON)

    def close(self):
        self.click_element(*HomePageLocator.CLOSE_BUTTON)

    def waiting(self, x):
        x = int(x)
        time.sleep(x)

    def buy(self, product):
        hover = ActionChains(self.driver).move_to_element(self.get_element(By.XPATH, '//*[contains(text(), "'+product+'")]'))
        hover.perform()
        self.click_element(*HomePageLocator.BUY_BUTTON)

    def shopping_cart(self):
        return self.get_element(*HomePageLocator.CART_MODAL)

    def promoshare_modal(self):
        return self.get_element(*HomePageLocator.PROMOSHARE_MODAL)

    def checkout(self):
        self.click_element(*HomePageLocator.CHECKOUT_BUTTON)

import time
from selenium.webdriver.common.by import By
from browser import Browser
from selenium.webdriver.common.action_chains import ActionChains

from pages.object_repository import ObjectRepository
from pages.public_library import PublicLibrary

class PublicPage(Browser):
    # Public Page Actions

    def test(self):
        obj     = ObjectRepository
        func    = PublicLibrary
        func.click_element(self, *obj.LOGIN_BUTTON)

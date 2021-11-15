from pages.locators import *
class Index():
    def __init__(self, chrome_webdriver):
        self.chrome_webdriver = chrome_webdriver
        self.locator = IndexLocator
    def search_contact(self):
        return self.chrome_webdriver.find_element(*self.locator.SEARCH_FIELD)

    def sent_message(self):
        return self.chrome_webdriver.find_element(*self.locator.MESSAGE_FIELD)

    def menu_button(self):
        return self.chrome_webdriver.find_element(*self.locator.MENU)

    def logout_button(self):
        return self.chrome_webdriver.find_element(*self.locator.LOGOUT)
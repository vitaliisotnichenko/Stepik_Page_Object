import time

from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from .locators import MainPageLocators

from .base_page import BasePage

class MainPage(BasePage):

    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

    def go_to_all_items(self):

       for i in range(3):
           try:
                self.browser.find_element(By.CSS_SELECTOR, "[data-navigation=dropdown-menu]>li:nth-child(1)").click()
                self.title_items = str(self.browser.find_element(By.CSS_SELECTOR, ".page-header.action>h1").text)
                return "Все товары" in self.title_items
           except (NoSuchElementException, StaleElementReferenceException):
               time.sleep(5)
               i += 1
               print("Couldn't find element. Retrying... " + str(i) + " attempt")


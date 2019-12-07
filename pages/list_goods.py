from selenium.webdriver.common.by import By
from .locators import MainPageLocators

from .base_page import BasePage

class ListGoods(BasePage):
    def click_on_the_good(self):
        self.browser.find_element(By.CSS_SELECTOR, ".col-xs-6:nth-child(1) h3").click()
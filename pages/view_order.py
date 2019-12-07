import time

from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

from pages.base_page import BasePage

class ViewOrder(BasePage):

    def confirm_order(self):
        self.browser.find_element_by_css_selector("#place-order").click()
        for i in range(3):
            try:
                text = self.browser.find_element_by_css_selector("#messages+div>h1").text
                return text
            except (NoSuchElementException, StaleElementReferenceException):
                time.sleep(5)
                i += 1
                print("Couldn't find element. Retrying... " + str(i) + " attempt")
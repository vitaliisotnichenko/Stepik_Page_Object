from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class CheckoutPage(BasePage):

    def enter_email_checkout(self, email):
        self.browser.find_element(By.CSS_SELECTOR, "[type=email]").send_keys(email)

    def enter_password_checkout(self, password):
        self.browser.find_element(By.CSS_SELECTOR, "[type=password]").send_keys(password)

    def click_submit_button_at_checkout(self):
        self.browser.find_element(By.CSS_SELECTOR, "[type=submit]").click()
        return self.browser.find_element(By.CSS_SELECTOR, "h1").text
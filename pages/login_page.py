import random
import string
import time

from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By

from .base_page import BasePage

class LoginPage(BasePage):

    def random_string(self):
        self.letters = string.ascii_lowercase
        return ''.join(random.choice(self.letters) for i in range(8))

    def registration_form_at_page(self):
        self.sign_up = self.browser.find_element_by_css_selector("#register_form>h2").text
        return "Зарегистрироваться" in self.sign_up

    def enter_email(self, email):
        for i in range(3):
            try:
                __email = self.browser.find_element(By.CSS_SELECTOR, "#id_registration-email")
                if __email.is_displayed():
                   return __email.send_keys(email + self.random_string() + "@gmail.com")

            except (NoSuchElementException, StaleElementReferenceException):
                time.sleep(5)
                i += 1
                print("Couldn't find element. Retrying... " + str(i) + " attempt")

    # def enter_email(self, email):
    #     self.browser.find_element(By.CSS_SELECTOR, "#id_registration-email").clear()
    #     self.browser.find_element(By.CSS_SELECTOR, "#id_registration-email").send_keys(email + self.random_string() + "@gmail.com")


    def enter_password(self, password):
        self.browser.find_element(By.CSS_SELECTOR, "#id_registration-password1").clear()
        self.browser.find_element(By.CSS_SELECTOR, "#id_registration-password1").send_keys(password)

    def confirm_password(self, password):
        self.browser.find_element_by_css_selector("#id_registration-password2").clear
        self.browser.find_element_by_css_selector("#id_registration-password2").send_keys(password)

    def click_on_confirm_registration_button(self):
        self.browser.find_element(By.CSS_SELECTOR, "[name=registration_submit]").click()

    def should_be_registration_success_message(self):
        self.success_message = self.browser.find_element(By.CSS_SELECTOR, ".alertinner.wicon").text
        return self.success_message
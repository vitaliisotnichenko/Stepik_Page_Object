from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class ItemDetailsPage(BasePage):

    def add_to_cart(self):
        self.browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket").click()

    def add_comment(self):
        self.browser.find_element(By.CSS_SELECTOR, "#reviews+p>a").click()
        return self.browser.find_element(By.CSS_SELECTOR, "legend").text

    def add_comment_title(self):
        self.browser.find_element(By.CSS_SELECTOR, "#id_title").send_keys("test")

    def add_comment_message(self):
        self.browser.find_element(By.CSS_SELECTOR, "#id_body").send_keys("test")

    def add_comment_name(self):
        self.browser.find_element(By.CSS_SELECTOR, "#id_name").send_keys("test")

    def add_comment_email(self):
        self.browser.find_element(By.CSS_SELECTOR, "#id_email").send_keys("test2@gmail.com")

    def click_add_comment_button(self):
        self.browser.find_element(By.CSS_SELECTOR, "[data-loading-text=\"Сохранение...\"]").click()
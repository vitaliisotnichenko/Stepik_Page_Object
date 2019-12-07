from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.base_page import BasePage

class DeliveryAddress(BasePage):

    def add_first_name_at_delivery_address_page(self, first_name):
        self.browser.find_element(By.CSS_SELECTOR, "#id_first_name").send_keys(first_name)

    def add_last_name_at_delivery_address_page(self, last_name):
        self.browser.find_element(By.CSS_SELECTOR, "#id_last_name").send_keys(last_name)

    def add_region_at_delivery_address_page(self, region):
        self.browser.find_element(By.CSS_SELECTOR, "#id_line1").send_keys(region)

    def add_city_at_delivery_address_page(self, city):
        self.browser.find_element(By.CSS_SELECTOR, "#id_line4").send_keys(city)

    def add_postal_code_at_delivery_address_page(self, postal_code):
        self.browser.find_element(By.CSS_SELECTOR, "#id_postcode").send_keys(postal_code)

    def choose_the_country_at_delivery_address_page(self, country):
        self.select = Select(self.browser.find_element_by_css_selector("select[name=country]"))
        self.select.select_by_value(country)

    def click_submit_button_at_delivery_address_page(self):
        self.browser.find_element(By.CSS_SELECTOR, "[type=submit]").click()
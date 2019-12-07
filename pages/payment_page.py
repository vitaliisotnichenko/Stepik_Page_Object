from pages.base_page import BasePage

class PaymentPage(BasePage):

    def add_payment(self):
        self.browser.find_element_by_css_selector("#view_preview").click()
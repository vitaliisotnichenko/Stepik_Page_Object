from pages.base_page import BasePage

class VerificationPage(BasePage):

    def proceed_order(self):
        self.browser.find_element_by_css_selector("p>a:nth-child(2)").click()
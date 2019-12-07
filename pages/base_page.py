from selenium.common.exceptions import NoSuchElementException


class BasePage():

    def __init__(self, browser, timeout=10):
        self.browser = browser
        self.browser.implicitly_wait(timeout)


    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True


    def open(self):
        self.browser.get("http://selenium1py.pythonanywhere.com/ru/")
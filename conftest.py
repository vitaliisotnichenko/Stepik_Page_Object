import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None)

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    language == "en"
    browser: WebDriver() = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    yield browser
    browser.quit()


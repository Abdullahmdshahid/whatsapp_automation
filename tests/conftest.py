import pytest
from selenium import webdriver


@pytest.fixture(scope='class')
def main(request):
    chrome_webdriver = webdriver.Chrome(executable_path=r"F:\whatsapp_automation\chromedriver_win32\chromedriver.exe")
    chrome_webdriver.get("https://web.whatsapp.com")
    chrome_webdriver.maximize_window()
    chrome_webdriver.implicitly_wait(180)

    request.cls.chrome_webdriver = chrome_webdriver
    yield
    chrome_webdriver.close()

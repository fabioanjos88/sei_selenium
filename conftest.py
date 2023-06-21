import pytest
from selenium import webdriver
driver: webdriver.Remote

@pytest.fixture

def setup_teardown():
    global driver
    options = webdriver.ChromeOptions()
    options.headless = True
    # driver = webdriver.Chrome(chrome_options=options)
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("https://homologacao.sei.sp.gov.br")

    yield
    driver.quit()
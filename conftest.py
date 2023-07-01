import pytest
from selenium import webdriver
from pages.login_page import LoginPage
driver: webdriver.Remote

@pytest.fixture

def setup_teardown():
    global driver
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument("--start-maximized")
    # driver = webdriver.Chrome(chrome_options=options) #PARA HEADLESS
    driver = webdriver.Chrome() #NAVEGADOR
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("https://homologacao.sei.sp.gov.br")

    yield
    driver.quit()
import pytest
import time
from pages.login_page import LoginPage
from pages.base_page import BasePage
from pages.home_page import HomePage

@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
@pytest.mark.regressivo

class TestSEI:
    def test_login(self):
        login_page = LoginPage()
        home_page = HomePage()
        
        login_page.fazer_login()
        home_page.aguardar_titulo()

import pytest
from pages.login_page import LoginPage
from pages.base_page import BasePage
from pages.home_page import HomePage

@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.CT01
@pytest.mark.CT01_02
@pytest.mark.regressivo

class TestSEI:
    def test_CT01_login_invalido(self):
        login_page = LoginPage()
        
        login_page.fazer_login_invalido()
        login_page.aceitar_alerta()
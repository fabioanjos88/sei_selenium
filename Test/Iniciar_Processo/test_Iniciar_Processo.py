import pytest
import time
from pages.login_page import LoginPage
from pages.base_page import BasePage
from pages.home_page import HomePage
from pages.iniciar_processo import IniciarProcesso
from pages.capa_processo import CapaProcesso



@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.iniciar_processo
@pytest.mark.regressivo

class TestSEI:
    def test_iniciar_processo(self):
        login_page = LoginPage()
        home_page = HomePage()
        iniciar_processo = IniciarProcesso()
        capa_processo = CapaProcesso()
        
        login_page.fazer_login()
        home_page.aguardar_titulo()
        home_page.clicar_inciar_processo()
        iniciar_processo.visualizar_todos_tipo()
        iniciar_processo.selecionar_tipo_documento()
        capa_processo.aguardar_tipo_processo()

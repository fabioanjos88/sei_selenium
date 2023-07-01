import pytest
import time
from pages.login_page import LoginPage
from pages.base_page import BasePage
from pages.home_page import HomePage
from pages.selecionar_processo import IniciandoProcesso
from pages.capa_processo import CapaProcesso


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.iniciar_processo
@pytest.mark.CT02
@pytest.mark.regressivo

class CriarProcesso:
    def criar_processo(self):
    # def test_criar_processo(self):
        login_page = LoginPage()
        home_page = HomePage()
        criar_processo = IniciandoProcesso()
        capa_processo = CapaProcesso()
        
        login_page.fazer_login()
        home_page.aguardar_carregar_titulo()
        home_page.clicar_inciar_processo()
        criar_processo.selecionar_tipo_documento("Estatuto")
        capa_processo.aguardar_carregar_tela_capa_processo()
        capa_processo.preencher_capa_processo()

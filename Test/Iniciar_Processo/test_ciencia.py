import pytest
import time
from pages.login_page import LoginPage
from pages.base_page import BasePage
from pages.home_page import HomePage
from pages.capa_processo import CapaProcesso
from pages.tela_processo import TelaProcesso
from pages.ciencia import Ciencia
from Test.Iniciar_Processo.criar_processo import CriarProcesso


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.ciencia
@pytest.mark.CT02
@pytest.mark.CT02_01
@pytest.mark.regressivo

class TestSEI:
    def test_ciencia(self):
        tela_processo = TelaProcesso()
        criar_processo = CriarProcesso()

        criar_processo.criar_processo()
        tela_processo.aguardar_icones_tela_processo()
        tela_processo.clicar_ciencia()


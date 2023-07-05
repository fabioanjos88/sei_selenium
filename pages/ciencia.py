from selenium.webdriver.common.by import By
import conftest
from pages.base_page import BasePage
from selenium.webdriver.support.select import Select
from datetime import datetime
from selenium.webdriver.common.keys import Keys
from pages.login_page import LoginPage


class Ciencia(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.data_atual = datetime.now()
        self.iframe_tela_ciencia = ("ifrVisualizacao")
        self.title_ciencia = (By.ID,"divInfraBarraLocalizacao")
        self.field_unidade = (By.XPATH, "//td[contains(.,'TESTE')]")
        self.field_usuario = (By.XPATH, "//td[contains(.,'fsanjos')]")
        self.field_descricao = (By.XPATH, "//td[contains(.,'Ciência no processo')]")

    def confirmar_ciencia(self):
        INFO_UNIDADE = (By.ID, "lnkInfraUnidade")
        self.ir_para_iframe_principal()
        self.selecionar_iframe(self.iframe_tela_ciencia)
        self.aguardar_elemento_visivel(self.title_ciencia)
        INFO_UNIDADE_CIENCIA = self.coletar_texto(self.field_unidade)
        self.comparar_texto(INFO_UNIDADE_CIENCIA, INFO_UNIDADE)
        INFO_USUARIO = self.coletar_texto(self.field_usuario)
        self.comparar_texto(INFO_USUARIO, 'fsanjos')
        INFO_DESCRICAO = self.coletar_texto(self.field_descricao)
        self.comparar_texto(INFO_DESCRICAO, "Ciência no processo")
        self.ir_para_iframe_principal()
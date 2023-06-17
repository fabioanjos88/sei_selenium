from selenium.webdriver.common.by import By
import conftest
from pages.base_page import BasePage
from selenium.webdriver.support.select import Select

class HomePage(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.title_controle_de_processo = (By.ID, "divInfraBarraLocalizacao")  
        self.btn_iniciar_processo = (By.XPATH, "//span[contains(.,'Iniciar Processo')]")

    def confirmacao_login(self):
        self.verificar_se_elemento_existe(self.title_controle_de_processo)

    def aguardar_titulo(self):
        self.aguardar_elemento(self.title_controle_de_processo)
        
    def confirmar_titulo(self):
        texto_titulo = self.encontrar_elemento(self.title_controle_de_processo).text
        assert texto_titulo == "Controle de Processos"

    def clicar_inciar_processo(self):
        self.aguardar_elemento(self.btn_iniciar_processo)
        self.clicar(self.btn_iniciar_processo)

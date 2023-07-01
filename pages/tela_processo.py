from selenium.webdriver.common.by import By
import conftest
from pages.base_page import BasePage
from selenium.webdriver.support.select import Select
from datetime import datetime
from selenium.webdriver.common.keys import Keys

class TelaProcesso(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.data_atual = datetime.now()
        self.iframe_icones = ("ifrVisualizacao")
        self.arvore_acoes = (By.ID, "divArvoreAcoes")
        self.btn_ciencia = (By.XPATH, "//img[contains(@alt,'Ciência')]")

    def aguardar_icones_tela_processo(self):
        self.selecionar_iframe(self.iframe_icones)
        self.aguardar_elemento_visivel(self.arvore_acoes)
    
    def clicar_ciencia(self):
        self.clicar(self.btn_ciencia)

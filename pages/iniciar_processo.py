from selenium.webdriver.common.by import By
import conftest
from pages.base_page import BasePage
from selenium.webdriver.support.select import Select
import time


class IniciarProcesso(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.btn_exibir_todos_tipos = (By.XPATH, "//img[contains(@title,'Exibir todos os tipos')]")
        self.field_pesquisa_tipo_documento = (By.XPATH, "//input[contains(@class,'infraAutoCompletar infraText ')]")
        
    def visualizar_todos_tipo(self):
        self.clicar(self.btn_exibir_todos_tipos)
    
    def selecionar_tipo_documento(self):
        self.escrever(self.field_pesquisa_tipo_documento, "Código")
        # Simular btn para baixo

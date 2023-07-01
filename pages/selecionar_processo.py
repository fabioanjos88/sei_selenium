from selenium.webdriver.common.by import By
import conftest
from pages.base_page import BasePage
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.common.keys import Keys

class IniciandoProcesso(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.btn_exibir_todos_tipos = (By.XPATH, "//img[contains(@title,'Exibir todos os tipos')]")
        self.field_pesquisa_tipo_documento = (By.XPATH, "//input[contains(@class,'infraAutoCompletar infraText ')]")
        
    def selecionar_tipo_documento(self, locator):
        self.clicar(self.btn_exibir_todos_tipos)
        self.escrever(self.field_pesquisa_tipo_documento, locator)
        self.encontrar_elemento(self.field_pesquisa_tipo_documento).send_keys(Keys.ARROW_DOWN, Keys.ENTER)
    
from selenium.webdriver.common.by import By
import conftest
from pages.base_page import BasePage
from selenium.webdriver.support.select import Select

class CapaProcesso(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.tipo_processo = (By.ID, "lblTipoProcedimento")

    def aguardar_tipo_processo(self):
        self.aguardar_elemento(self.tipo_processo)
        

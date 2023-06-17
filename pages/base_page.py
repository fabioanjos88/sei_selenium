import select
import conftest
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

class BasePage:
    def __init__(self):
        self.driver = conftest.driver

    def encontrar_elemento(self, locator):
        return self.driver.find_element(*locator)
    
    def encontrar_elementos(self, locator):
        return self.driver.find_elements(*locator)
    
    def escrever(self, locator, text):
        self.encontrar_elemento(locator).send_keys(text)
    
    def clicar(self, locator):
        self.encontrar_elemento(locator).click()
    
    def verificar_se_elemento_existe(self, locator):
        assert self.encontrar_elemento(locator).is_displayed(), "Não localizado!"
    
    def dropdown(self, locator, text):
        dropdown = Select(self.encontrar_elemento(locator))
        dropdown.select_by_visible_text(text)
    
    def accept_alert(self):
        wait = WebDriverWait(self.driver, 7)
        wait.until(EC.alert_is_present())
        alerta = self.driver.switch_to.alert
        alerta.accept()

    def aguardar_elemento(self, locator):
        wait = WebDriverWait(self.driver, 7)
        wait.until(EC.presence_of_element_located(locator))   
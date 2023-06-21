from selenium.webdriver.common.by import By
import conftest
from pages.base_page import BasePage
from selenium.webdriver.support.select import Select
import time


class LoginPage(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.usuario = "fsanjos"
        self.senha = "fsanjos"
        self.senha_errada = "senhaErrada"
        self.orgao_padrao = "GESP"
        self.field_username = (By.ID, "txtUsuario")
        self.field_password = (By.ID, "pwdSenha")
        self.btn_acessar = (By.ID, "Acessar")
        self.logo_sei_login = (By.ID, "divLogo")
        self.dropdwon_orgao = (By.ID, "selOrgao")
        
    def fazer_login(self):     
        self.escrever(self.field_username, self.usuario)
        self.escrever(self.field_password, self.senha)
        self.dropdown(self.dropdwon_orgao, self.orgao_padrao)
        self.clicar(self.btn_acessar)
    
    def fazer_login_invalido(self):
        self.verificar_se_elemento_existe(self.logo_sei_login)
        self.escrever(self.field_username, self.usuario)
        self.escrever(self.field_password, self.senha_errada)
        self.dropdown(self.dropdwon_orgao, self.orgao_padrao)
        self.clicar(self.btn_acessar)

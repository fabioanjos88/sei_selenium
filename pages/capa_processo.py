from selenium.webdriver.common.by import By
import conftest
from pages.base_page import BasePage
from selenium.webdriver.support.select import Select
from datetime import datetime
from selenium.webdriver.common.keys import Keys

class CapaProcesso(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.data_atual = datetime.now()
        self.tipo_processo = (By.ID, "lblTipoProcedimento")
        self.field_especificacao = (By.ID, "txtDescricao")
        self.field_interessados = (By.ID, "txtInteressadoProcedimento")
        self.field_observacoes = (By.ID, "txaObservacoes")
        self.radio_publico = (By.ID, "divOptPublico")
        self.btn_salvar = (By.ID, "btnSalvar")
        self.iframe_informacoes_processo = ("ifrArvore")
        self.numero_processo = (By.ID, "header")

    def aguardar_carregar_tela_capa_processo(self):
        self.aguardar_elemento_visivel(self.tipo_processo)
    
    def preencher_capa_processo(self):
        self.encontrar_elemento(self.field_especificacao)
        self.escrever(self.field_especificacao, f"(DESCRIÇÂO) Teste {self.data_atual.date()}")
        self.escrever(self.field_interessados, f"(INTERESSADOS) Teste {self.data_atual.date()}")
        self.escrever(self.field_interessados, f"(INTERESSADOS) Teste {self.data_atual}")
        self.encontrar_elemento(self.field_interessados).send_keys(Keys.ENTER)
        self.aceitar_alerta()
        self.escrever(self.field_observacoes, f"(OBSERVAÇÕES) Teste {self.data_atual.date()}")
        self.clicar(self.radio_publico)
        self.clicar(self.btn_salvar)
        self.selecionar_iframe(self.iframe_informacoes_processo)
        numero_do_processo = self.encontrar_elemento(self.numero_processo).text
        print(numero_do_processo)
        self.ir_para_iframe_principal()




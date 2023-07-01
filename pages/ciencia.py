from selenium.webdriver.common.by import By
import conftest
from pages.base_page import BasePage
from selenium.webdriver.support.select import Select
from datetime import datetime
from selenium.webdriver.common.keys import Keys

class Ciencia(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.data_atual = datetime.now()
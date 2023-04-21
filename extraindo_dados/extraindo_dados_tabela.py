import time

from selenium import webdriver as webDriver
from selenium.webdriver.common.by import By

navegador = webDriver.Chrome()

navegador.get("https://rpachallengeocr.azurewebsites.net/")
time.sleep(4)

elementoTabela = navegador.find_element(by=By.XPATH, value='//*[@id="tableSandbox"]')

linhas = elementoTabela.find_elements(by=By.TAG_NAME, value='tr')

coluna = elementoTabela.find_elements(by=By.TAG_NAME, value='td')

linha = 1
for linhaAtual in linhas:
    print(linhaAtual.text)

    linha += 1

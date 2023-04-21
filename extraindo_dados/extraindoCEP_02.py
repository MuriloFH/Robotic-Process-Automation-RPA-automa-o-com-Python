import sys

from selenium import webdriver as webDriver
from selenium.webdriver.common.by import By
import time

navegador = webDriver.Chrome()

while True:
    navegador.get("https://buscacepinter.correios.com.br/app/endereco/index.php")

    time.sleep(2)

    # inserindo o cep na caixa de pesquisa
    navegador.find_element(By.NAME, "endereco").send_keys('88812495')

    time.sleep(2)

    # pesquisando
    navegador.find_element(By.NAME, 'btn_pesquisar').click()

    time.sleep(2)

    # coletando os elementos da tabela do resultado
    elementoTabela = navegador.find_element(By.XPATH, '//*[@id="resultado-DNEC"]')

    # percorrendo cada linha e colunas da tabela
    for linha in elementoTabela.find_elements(By.TAG_NAME, 'tr'):
        endereco = ""
        for coluna in linha.find_elements(By.TAG_NAME, 'td'):
            # coletando as informações e colocando na variável pra usar depois
            endereco += ";" + coluna.text
        print(endereco)
    imput = input("Continuar? S/N\n")

    if imput == "N":
        sys.exit()




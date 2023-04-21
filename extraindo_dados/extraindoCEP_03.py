import sys

from selenium import webdriver as webDriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

listaDataFrame = []

navegador = webDriver.Chrome()

while True:
    navegador.get("https://buscacepinter.correios.com.br/app/endereco/index.php")

    time.sleep(2)
    dicCep = {
        "cep1": "57040692",
        "cep2": "69053281",
        "cep3": "49020430"
    }
    # inserindo o cep na caixa de pesquisa
    navegador.find_element(By.NAME, "endereco").send_keys("57040692")

    time.sleep(2)

    # pesquisando
    navegador.find_element(By.NAME, 'btn_pesquisar').click()

    time.sleep(2)

    # percorrendo cada linha e colunas da tabela
    for contador in dicCep.values():

        # voltando para a pagina inicial
        navegador.find_element(By.ID, 'btn_nbusca').click()
        time.sleep(2)

        # inserindo o cep na caixa de pesquisa
        navegador.find_element(By.NAME, "endereco").send_keys(contador)

        time.sleep(2)

        # pesquisando
        navegador.find_element(By.NAME, 'btn_pesquisar').click()

        time.sleep(2)

        # coletando os elementos da tabela do resultado
        elementoTabela = navegador.find_element(By.XPATH, '//*[@id="resultado-DNEC"]')
        endereco = ""
        for linha in elementoTabela.find_elements(By.TAG_NAME, 'tr'):
            for coluna in linha.find_elements(By.TAG_NAME, 'td'):
                # coletando as informações e colocando na variável pra usar depois
                endereco += ";" + coluna.text

        listaDataFrame.append(endereco)
        print(endereco)
    imput = input("Continuar? S/N\n")
    if imput == "N":
        break


arquivoExcel = pd.ExcelWriter("EnderecosBuscaCEP.xlsx", engine='xlsxwriter')
arquivoExcel.save()

dataFrame = pd.DataFrame(listaDataFrame, columns=[';rua;bairro;cidade;cep'])

# preparando o aquivo
arquivoExcel = pd.ExcelWriter("EnderecosBuscaCEP.xlsx", engine='xlsxwriter')
# convertendo o data frame em um objeto excel
dataFrame.to_excel(arquivoExcel, sheet_name="Dados", index=False)

arquivoExcel.save()



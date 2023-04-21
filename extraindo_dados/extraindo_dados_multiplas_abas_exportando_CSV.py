import time
import pandas as pd

from selenium import webdriver as webDriver
from selenium.webdriver.common.by import By

listaDataFrame = []

navegador = webDriver.Chrome()

navegador.get("https://rpachallengeocr.azurewebsites.net/")
time.sleep(4)

i = 1
linha = 1
while i < 4:

    elementoTabela = navegador.find_element(by=By.XPATH, value='//*[@id="tableSandbox"]')

    linhas = elementoTabela.find_elements(by=By.TAG_NAME, value='tr')

    coluna = elementoTabela.find_elements(by=By.TAG_NAME, value='td')

    print(f"Pagina {i}")
    for linhaAtual in linhas:
        print(linhaAtual.text)
        listaDataFrame.append(linhaAtual.text)

        linha += 1

    i += 1

    time.sleep(2)

    # procurando o xpath do botão proximo
    navegador.find_element(by=By.XPATH, value='//*[@id="tableSandbox_next"]').click()
    time.sleep(2)

else:
    print("Finalizado!")

arquivoCSV = pd.ExcelWriter(path="dadosAbasSite.csv", engine="xlsxwriter")
arquivoCSV.save()

dataFrame = pd.DataFrame(data=listaDataFrame, columns=['#;id;Due Date'])

arquivoCSV = pd.ExcelWriter(path="dadosAbasSite.csv", engine="xlsxwriter")

dataFrame.to_excel(arquivoCSV, sheet_name="dados", index=False)

arquivoCSV.save()


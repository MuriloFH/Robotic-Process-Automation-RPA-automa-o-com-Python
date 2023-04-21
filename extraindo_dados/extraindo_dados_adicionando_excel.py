import time

from selenium import webdriver as webDriver
from selenium.webdriver.common.by import By
import pandas

navegador = webDriver.Chrome()

navegador.get("https://rpachallengeocr.azurewebsites.net/")
time.sleep(4)

elementoTabela = navegador.find_element(by=By.XPATH, value='//*[@id="tableSandbox"]')

linhas = elementoTabela.find_elements(by=By.TAG_NAME, value='tr')

coluna = elementoTabela.find_elements(by=By.TAG_NAME, value='td')

dataFrameList = []
linha = 1
for linhaAtual in linhas:
    dataFrameList.append(linhaAtual.text)
    print(linhaAtual.text)

    linha += 1

arquivoExcel = pandas.ExcelWriter('dadosSite.xlsx', engine='xlsxwriter')
arquivoExcel.save()

dataFram = pandas.DataFrame(data=dataFrameList, columns=['Dados'])

# preparando o arquivo do excel
arquivoExcel = pandas.ExcelWriter('dadosSite.xlsx', engine='xlsxwriter')

dataFram.to_excel(arquivoExcel, sheet_name='Sheet1', index=False)

arquivoExcel.save()


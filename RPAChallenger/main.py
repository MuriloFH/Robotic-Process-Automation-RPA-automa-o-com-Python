from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from openpyxl import load_workbook

# abrindo o arquivo
nomeArquivoDados = "challenge.xlsx"
planilhaDadosAlunos = load_workbook(nomeArquivoDados)
# selecionando a planilha
sheetSelecionada = planilhaDadosAlunos["Sheet1"]

# preparando navegador
navegador = webdriver.Chrome()
navegador.get("https://www.rpachallenge.com/")
navegador.maximize_window()

# time.sleep(2)

for linhaPlanilha in range(2, len(sheetSelecionada["A"]) + 1):
    time.sleep(2)

    primeiroNome = sheetSelecionada['A%s' % linhaPlanilha].value
    ultimoNome = sheetSelecionada['B%s' % linhaPlanilha].value
    nomeEmpresa = sheetSelecionada['C%s' % linhaPlanilha].value
    cargo = sheetSelecionada['D%s' % linhaPlanilha].value
    endereco = sheetSelecionada['E%s' % linhaPlanilha].value
    email = sheetSelecionada['F%s' % linhaPlanilha].value
    NumeroTelefone = sheetSelecionada['G%s' % linhaPlanilha].value

    if primeiroNome is None:
        break

    listCamposPlanilha = [primeiroNome, ultimoNome, nomeEmpresa, cargo, endereco, email, NumeroTelefone]
    listCamposSite = ["labelFirstName", "labelLastName", "labelCompanyName", "labelRole", "labelAddress", "labelEmail", "labelPhone"]

    for i in range(0, len(listCamposSite)):
        navegador.find_element(By.XPATH, f'//*[@ng-reflect-name="{listCamposSite[i]}"]').send_keys(listCamposPlanilha[i])
        time.sleep(0.5)

    navegador.find_element(By.XPATH, '/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/input').click()

    # primeiroNome
    # navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelFirstName"]').send_keys(primeiroNome)
    # time.sleep(0.5)
    #
    # # ultimoNome
    # navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelLastName"]').send_keys(ultimoNome)
    # time.sleep(0.5)
    #
    # # nomeEmpresa
    # navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelCompanyName"]').send_keys(nomeEmpresa)
    # time.sleep(0.5)
    #
    # # cargo
    # navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelRole"]').send_keys(cargo)
    # time.sleep(0.5)
    #
    # # endereco
    # navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelAddress"]').send_keys(endereco)
    # time.sleep(0.5)
    #
    # # email
    # navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelEmail"]').send_keys(email)
    # time.sleep(0.5)
    #
    # # NumeroTelefone
    # navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelPhone"]').send_keys(NumeroTelefone)
    # time.sleep(0.5)

    # navegador.find_element(By.XPATH, '/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/input').click()


navegador.close()
print("Desafio finalizado!")

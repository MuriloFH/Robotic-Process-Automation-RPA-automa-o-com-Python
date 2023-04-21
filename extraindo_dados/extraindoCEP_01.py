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

    rua = navegador.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[1]').text
    print(rua)

    bairro = navegador.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[2]').text
    print(bairro)

    cidade = navegador.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[3]').text
    print(cidade)

    cep = navegador.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[4]').text
    print(cep)

    imput = input("Continuar? S/N")

    if imput == "N":
        sys.exit()




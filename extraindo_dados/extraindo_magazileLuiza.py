import time

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

listDataFrame = []
navegador = webdriver.Chrome()

nomeProduto = "iphone+13+128gb"
navegador.get(f'https://www.magazineluiza.com.br/busca/{nomeProduto}/')
time.sleep(2)
print("pesquisou pelo produto")

listProdutos = navegador.find_elements(By.CLASS_NAME, "fwviCj")

listnomeProduto = []
listprecoOriginal = []
listprecoDesconto = []
listurlProduto = []

for iten in listProdutos:

    nomeProduto = None
    precoOriginal = None
    precoDesconto = None
    urlProduto = None

    if nomeProduto is None:
        try:
            nomeProduto = iten.find_element(By.CLASS_NAME, value="hQYVAI").text
        except Exception:
            pass
    elif nomeProduto is None:
        try:
            nomeProduto = iten.find_element(By.CLASS_NAME, value="sc-hFVsQR").text
        except:
            nomeProduto = "Errooooooooooooooooooooooooooooooooooooooooooooooooooooooo"
            pass

    # preço original
    classPrecoOriginal = "gcLiKJ sc-ehkVkK jxmyPO"
    classPrecoOriginal = classPrecoOriginal.split(" ")
    for i in range(len(classPrecoOriginal)):
        if precoOriginal is None:
            try:
                precoOriginal = iten.find_element(by=By.CLASS_NAME, value=classPrecoOriginal[i]).text
            except:
                precoOriginal = "R$ 0"
                pass

    # preço desconto
    classPrecoDesconto = "jDmBNY sc-hGglLj bQqJoc"
    classPrecoDesconto = classPrecoDesconto.split(" ")
    for i in range(len(classPrecoDesconto)):
        if precoDesconto is None:
            try:
                precoDesconto = iten.find_element(by=By.CLASS_NAME, value=classPrecoDesconto[i]).text
            except:
                precoDesconto = "R$ 0"
                pass

    # url produto
    if urlProduto is None:
        try:
            urlProduto = iten.find_element(by=By.TAG_NAME, value="a").get_attribute("href")
        except:
            urlProduto = "Errooooooooooooooooooooooooooooooooooooooooooooooooooooooo"
            pass

    print("-" * 1000)
    print("Nome produto: ", nomeProduto)
    print("Preço original: ", precoOriginal)
    print("Preço com desconto: ", precoDesconto)
    print("Link do produto: ", urlProduto)

    listnomeProduto.append(nomeProduto)
    listprecoOriginal.append(precoOriginal)
    listprecoDesconto.append(precoDesconto)
    listurlProduto.append(urlProduto)

dic = {
    "Nome produto: ": listnomeProduto,
    "Preço original: ": listprecoOriginal,
    "Preço com desconto: ": listprecoDesconto,
    "Link do produto: ": listurlProduto,
}

print(dic)

arquivoCSV = pd.DataFrame(dic)
print(arquivoCSV)
arquivoCSV.to_csv(path_or_buf="arquivoMagaluuuuu.csv", sep=";", index=False)

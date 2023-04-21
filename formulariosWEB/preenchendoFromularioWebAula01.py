from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

navegador = webdriver.Chrome()

navegador.get("https://form.jotform.com/221436066464051")

time.sleep(4)

# preenchendo o campo nome
navegador.find_element(By.NAME, "q3_nome[first]").send_keys("Murilo Henrique")

time.sleep(1)

# preenchendo o sobre nome
navegador.find_element(By.NAME, "q3_nome[last]").send_keys("Fernandes")

time.sleep(1)

# preenchendo o campo e-mail
navegador.find_element(By.NAME, "q4_email").send_keys("murilohf19@gmail.com")

time.sleep(2)

# preenchendo o estado civil
pegaDropdown = navegador.find_element(By.ID, "input_5")
itemSelecionado = Select(pegaDropdown)
itemSelecionado.select_by_index(2)

time.sleep(2)

# preenchendo o tem filhos?
filho = "Não"
if filho == "Sim":
    navegador.find_element(By.ID, "label_input_6_0").click()
else:
    navegador.find_element(By.ID, "label_input_6_1").click()

time.sleep(1)

# selecionando a cor
navegador.find_element(By.ID, "label_input_7_2").click()

time.sleep(1)

# selecionando a avaliacao
navegador.find_element(By.XPATH, '//*[@id="input_8"]/div[5]').click()

time.sleep(1)

# avaliando a qualidade do serviço
navegador.find_element(By.XPATH, '//*[@id="input_9_0_2"]').click()

time.sleep(1)

# avaliando o grau de dificuldade
navegador.find_element(By.XPATH, '//*[@id="input_9_1_1"]').click()

time.sleep(5)




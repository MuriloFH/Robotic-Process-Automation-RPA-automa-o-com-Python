import time

from selenium import webdriver as webDriver
from selenium.webdriver.common.by import By

navegador = webDriver.Chrome()

navegador.get("https://www.google.com.br/")

time.sleep(4)


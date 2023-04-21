import pyautogui

# clicando no iniciar do windows
pyautogui.moveTo(x=14, y=1067, duration=0.25)
pyautogui.click()

# pesquisando pelo chrome
pyautogui.sleep(seconds=1)
pyautogui.typewrite(message="chrome", interval=0.15)
pyautogui.sleep(seconds=1)
pyautogui.press(keys='enter')

# movendo o mouse para escolher o perfil do chrome
pyautogui.sleep(seconds=1)
pyautogui.moveTo(x=776, y=602, duration=0.15)
pyautogui.click()

# clicando na barra de endereço e pesquisando pela cotacao
pyautogui.sleep(seconds=1)
pyautogui.moveTo(x=2229, y=158, duration=0.15)
pyautogui.click()
pyautogui.typewrite("cotacao dolar", interval=0.15)
pyautogui.press('enter')



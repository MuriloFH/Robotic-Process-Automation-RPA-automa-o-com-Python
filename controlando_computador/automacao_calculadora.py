import pyautogui

pyautogui.sleep(seconds=2)
print(pyautogui.position())

# clicando no iniciar do windows
pyautogui.moveTo(x=14, y=1067, duration=0.15)
pyautogui.click()

# pesquisando pela calculadora
pyautogui.sleep(seconds=1)
pyautogui.typewrite(message="calculadora", interval=0.15)

# movendo e clicando na calculadora
pyautogui.sleep(seconds=1)
pyautogui.moveTo(x=175, y=390, duration=0.15)
pyautogui.click()


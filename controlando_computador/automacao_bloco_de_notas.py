import pyautogui

# Windows + r
pyautogui.hotkey('win', 'r')
pyautogui.sleep(1)

# digitando o que quero
pyautogui.typewrite('notepad', interval=0.10)
pyautogui.press('enter')
pyautogui.sleep(1)

# digitando no notepad
pyautogui.typewrite("Oláaa", interval=0.15)
pyautogui.sleep(1)

# fechando a janela ativa
pyautogui.hotkey('alt', 'f4')
pyautogui.sleep(0.5)
pyautogui.press('tab')
pyautogui.sleep(0.5)
pyautogui.press('enter')


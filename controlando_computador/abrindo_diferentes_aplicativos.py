import pyautogui


def abreOpcoes(opcao):
    pyautogui.sleep(2)
    pyautogui.press('win')
    pyautogui.sleep(0.5)

    pyautogui.typewrite(opcao, interval=0.10)
    pyautogui.press('enter')


opcao = pyautogui.confirm(text="clique no botão desejado", buttons=['Postman', 'bloco de notas', 'Chrome'])

if opcao == "Postman":
    abreOpcoes(opcao=opcao)
    print("Postman")
elif opcao == 'bloco de notas':
    abreOpcoes(opcao=opcao)
    print('bloco de notas')
else:
    abreOpcoes(opcao=opcao)
    print('Chrome')


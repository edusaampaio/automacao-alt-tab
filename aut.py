import pyautogui
import keyboard
import time

print('Inicando automação... pressione f para Parar')

try:
    while True: 
        if keyboard.is_pressed('f'):
            print('automação finalizada.')
            break


        pyautogui.keyDown('alt')
        pyautogui.press('tab')
        pyautogui.keyUp('alt')

        print('alternando entre janelas...(ALT + TAB)')
        time.sleep(5)

except KeyboardInterrupt:
    print('Interrompido manualmente') 
import pyautogui
import keyboard
import time

print('Inicando automação... pressione ESC para Parar')

try:
    while True: 
        if keyboard.is_pressed('space'):
            print('automação finalizada.')
            break


        pyautogui.keyDown('alt')
        pyautogui.press('tab')
        pyautogui.keyUp('alt')

        print('alternando entre janelas...(ALT + TAB)')
        time.sleep(5)

except KeyboardInterrupt:
    print('Interrompido manualmente')
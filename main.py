import pyautogui
import time

while True:
    time.sleep(10)
    pyautogui.drag(150, 150, 1, button='left')
    time.sleep(1)
    pyautogui.click(button="right")
    time.sleep(0.5)
    pyautogui.move(-150, -150, 0.5)
    time.sleep(0.5)
    pyautogui.moveTo(1000,1000)
    time.sleep(0.5)
    pyautogui.moveTo(500,500)

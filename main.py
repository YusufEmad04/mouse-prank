import pyautogui
import time

while True:
    time.sleep(10)
    pyautogui.drag(150, 150, 1, button='left')
    time.sleep(1)
    pyautogui.click(button="right")
    pyautogui.drag(-150, -150, 0.5)

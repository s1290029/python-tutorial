import time
import pyautogui

time.sleep(5)
pyautogui.click()

distance = 300
change = 30

while distance > 0:
    pyautogui.drag(distance, 0, duration=0.2)
    distance -= change
    pyautogui.drag(0, distance, duration=0.2)
    pyautogui.drag(-distance, 0, duration=0.2)
    distance -= change
    pyautogui.drag(0, -distance, duration=0.2)

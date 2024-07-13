import pyautogui

#get screen resolution
resolution = pyautogui.size()
print(resolution)

#get mouse position
mouse_pos = pyautogui.position()
print(mouse_pos)

#To see mouse information
pyautogui.mouseInfo()

#To know color in RGB
print(pyautogui.pixel(mouse_pos[0], mouse_pos[1]))

#To check color matching
if pyautogui.pixelMatchesColor(mouse_pos[0], mouse_pos[1], (255, 255, 255)):
    print("You are pointing at black color.")
else:
    print("You are not pointing at black color.")

#click
pyautogui.click()

#scroll
pyautogui.scroll(200)

#moveTo specific x, y place
for i in range(2):
    pyautogui.moveTo(100, 100, duration=0.5)
    pyautogui.moveTo(200, 100, duration=0.5)
    pyautogui.moveTo(200, 200, duration=0.5)
    pyautogui.moveTo(100, 200, duration=0.5)

#move vecter from current place
for i in range(2):
    pyautogui.move(100, 0, duration=0.5)
    pyautogui.move(0, 100, duration=0.5)
    pyautogui.move(-100, 0, duration=0.5)
    pyautogui.move(0, -100, duration=0.5)


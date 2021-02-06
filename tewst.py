import pyautogui
import time

time.sleep(0.1)
print(pyautogui.position())
pyautogui.hotkey("winleft", "r")
time.sleep(0.1)
pyautogui.typewrite("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
time.sleep(0.1)
pyautogui.press("enter")

import pyautogui
import time

a = ["Hackerbuoooyyyyy"]
time.sleep(5)
for i in range(30):
    pyautogui.typewrite(a[i%1])
    pyautogui.typewrite("\n")
    time.sleep(1)
    
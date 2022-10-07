import pyautogui
import time
import subprocess


subprocess.Popen(r"C:\Program Files (x86)\AudioRelay\AudioRelay.exe")

time.sleep(5)
location = pyautogui.locateOnScreen(r"C:\Users\eladc\Desktop\VOR\voice-regonition-command\player_image.PNG")
pyautogui.click(location)

time.sleep(2)
location = pyautogui.locateOnScreen(r"C:\Users\eladc\Desktop\VOR\voice-regonition-command\connect_image.PNG")
pyautogui.click(location)

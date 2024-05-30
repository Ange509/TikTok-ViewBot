import pyautogui
import time
import os
import requests
import pyperclip
import pyautogui

lien = input("Link of your tiktok video : ")
https://www.tiktok.com/@angelson3578/photo/7320005901190958368?is_from_webapp=1&sender_device=pc&web_id=7374883713279215136

for i in range (200):

    os.system("start tiktok")
    time.sleep(1)
    pyperclip.copy(f"{lien}")
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press("enter")
    time.sleep(300)
    os.system("taskkill /IM tiktok.exe")

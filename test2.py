import webbrowser
import pyautogui
import time
from tkinter import Tk
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.chrome import service
import webdriver_manager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import os




litery=[]
literasrodkowa=[]


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://spellsbee.com")
content = driver.page_source
soup = BeautifulSoup(content, 'html.parser')

for i in range(0,7):
    button_list = soup.find('button', {"id":f"key-{i}"})
    button_list_text = button_list.text
    print(button_list_text)
    if i != 3:
        litery.append(button_list_text)
    elif i == 3:
        literasrodkowa.append(button_list_text.lower())

print(litery)
print(literasrodkowa)


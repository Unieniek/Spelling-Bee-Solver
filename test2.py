import webbrowser
import pyautogui
import time
from tkinter import Tk
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.chrome import service
input_letter_list = []

#webbrowser.open('https://spellsbee.com', new=2)
#time.sleep(3)

litery=[] #List to store name of the product


#driver = webdriver.Chrome("/usr/lib/operagx-browser/chromedriver")
driver = webdriver.Chrome()
driver.get("https://spellsbee.com")
content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll('a',href=True, attrs={'button'}):
    key0=a.find('div', attrs={'button':'key-0'})

print(litery)



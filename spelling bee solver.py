import sys
from tqdm import tqdm
import urllib
import webbrowser
import pyautogui
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from bs4 import BeautifulSoup

#some lists
wordlistfinal = []
grayletterlist = []
yellowletterlist = []
list2=[]

print("Welcome to the amazing spelling bee solver")

#open file containing word list
with open('words_alpha.txt') as f_obj:
    list = f_obj.read().split()

#create a driver for opening browser
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#open browser link
driver.get("https://spellsbee.com")
content = driver.page_source
#copy page content
soup = BeautifulSoup(content, 'html.parser')

#check the page for
for i in range(0,7):
    #find button with a certain id i website source code
    button_list = soup.find('button', {"id":f"key-{i}"})
    #get the text out of a button
    button_list_text = button_list.text
    print(button_list_text)
    if i != 3:
        #fourth letter is the middle one
        grayletterlist.append(button_list_text)
    elif i == 3:
        yellowletterlist.append(button_list_text.lower())

print(f'Your gray letters are: {grayletterlist}')
print(f'Your yellow letters are: {yellowletterlist}')

#creating a string out of a table
yellowletter = ''.join(yellowletterlist)

#checking if the word contains more than the provided letters
flag=0
for line in list:
    for char in line:
        if char in grayletterlist or char == yellowletter:
            flag=1
        else:
            flag=0
            break
    if flag==1:
        if (yellowletter in line and len(line) > 3):
            list2.append(line)
            flag = 0

#automatic input
x,y = pyautogui.size()
#open browser window
webbrowser.open("https://spellsbee.com")
#wait 2 seconds for the page to load
time.sleep(2)
#click inside the page
pyautogui.click(x/4, y/4)

#inputing all of the letters into the game
for i in range(0, len(list2)):
    for letter in list2[i]:
        wordlistfinal.append(letter)
        pyautogui.typewrite(letter)
    pyautogui.typewrite(["enter"])

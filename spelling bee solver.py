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

#whole alphabet
#letters = ("a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,q,p,r,s,t,u,w,x,y,z").split(",")
letters = ("abcdefghijklmnoqprstuwvxyz")
letterslst = []
wordlistfinal = []
grayletterlist = []
yellowletterlist = []

print("Welcome to the amazing spelling bee solver")
#open file containing word list
with open('words_alpha.txt') as f_obj:
    lista = f_obj.read().split()
with open('words_alpha.txt') as f_obj:
    lista2 = f_obj.read().split()
with open('words_alpha.txt') as f_obj:
    lista3 = f_obj.read().split()

#create a driver for opening browser
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#open browser link
driver.get("https://spellsbee.com")
content = driver.page_source
#copy page content
soup = BeautifulSoup(content, 'html.parser')

#add alphabet letters to the list
for letter in letters:
    letterslst.append(letter)

#check the page for
for i in range(0,7):
    button_list = soup.find('button', {"id":f"key-{i}"})
    button_list_text = button_list.text
    print(button_list_text)
    if i != 3:
        grayletterlist.append(button_list_text)
    elif i == 3:
        yellowletterlist.append(button_list_text.lower())

print(f'Your gray letters are: {grayletterlist}')
print(f'Your yellow letters are: {yellowletterlist}')

#deleting letters from a alphabet string
for i in range(0, len(letters)):
    for j in range(0, len(grayletterlist)):
        if letters[i] in grayletterlist or letters[i] in yellowletterlist:
            letterslst.remove(letters[i])
            break

#checking if the word contains more than the provided letters
for i in tqdm(range(0, len(lista))):
    for j in range(0, len(letterslst)):
        if letterslst[j] in lista [i]:
            lista2.remove(lista[i])
            break

lista3 = lista2.copy()
yellowletter = ''.join(yellowletterlist)
#checking if the words have middle letter in them
for i in range(0, len(lista2)):
    if yellowletter not in lista2[i] or len(lista2[i])<=3:
        lista3.remove(lista2[i])

print(lista3)
#automatic input
webbrowser.open('https://spellsbee.com', new=2)
x,y = pyautogui.size()

time.sleep(2)
pyautogui.click(x/4, y/4)

for i in range(0, len(lista3)):
    for letter in lista3[i]:
        wordlistfinal.append(letter)
        pyautogui.typewrite(letter)
    pyautogui.typewrite(["enter"])

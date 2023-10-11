import sys
from tqdm import tqdm
import urllib
import webbrowser
import pyautogui
import time

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

#letter input
letter_input= input("Input 6 letters that are in gray hexagons: ")
middle_letter = input("Input the middle letter that is yellow hexagons: ")

for letter in letter_input:
    grayletterlist.append(letter)
for letter in middle_letter:
    yellowletterlist.append(letter)

print(f'Your gray letters are: {grayletterlist}')
print(f'Your yellow letters are: {yellowletterlist}')
#create a list for letters
for letter in letters:
    letterslst.append(letter)

#deleting letters from a alphabet string
for i in range(0, len(letters)):
    for j in range(0, len(letter_input)):
        if letters[i] in letter_input or letters[i] in middle_letter:
            letterslst.remove(letters[i])
            break


# print(str(letterslst))
# print(len(lista))
# print(len(letterslst))

#checking if the word contains more than the provided letters
for i in tqdm(range(0, len(lista))):
    for j in range(0, len(letterslst)):
        if letterslst[j] in lista [i]:
            lista2.remove(lista[i])
            #lista3.remove(lista[i])
            break

lista3 = lista2.copy()

#checking if the words have middle letter in them
for i in range(0, len(lista2)):
    if middle_letter not in lista2[i] or len(lista2[i])<=3:
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

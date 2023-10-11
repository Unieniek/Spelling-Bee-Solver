import webbrowser
import pyautogui
import time
from tkinter import Tk
input_letter_list = []
x,y = pyautogui.size()

webbrowser.open('https://spellsbee.com', new=2)
time.sleep(3)
pyautogui.click(x/4 + 100, y/4)
#time.sleep(1)
#pyautogui.hotkey(["ctrl", "shift", "i"])
pyautogui.dragTo((x-(x/4)), y-(y/2), duration=2)
pyautogui.hotkey(["ctrl", "c"])

root = Tk()
root.withdraw()
result = root.clipboard_get()

for letter in result:
    input_letter_list.append(letter)

k=len(input_letter_list) - 7

for i in range(0, k):
    del input_letter_list[-1]

print(input_letter_list)
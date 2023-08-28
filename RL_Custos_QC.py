import keyboard
import pyautogui as key
from pyautogui import typewrite
import time


f = open('QuickChats.txt','r')
word_list = f.readlines()

print(word_list)
            
def write_QC(text):
    i = 0
    while i < 3:
        key.press('t')
        typewrite(text)
        key.press('enter')
        i+=1

while True:

    ver = keyboard.read_key() 

    if ver == 'q':
        break
    elif ver == '5':
        write_QC(word_list[0])
    elif ver == '6':
        write_QC(word_list[1])
    elif ver == '7':
        write_QC(word_list[2])
    elif ver == '8':
        write_QC(word_list[3])

    time.sleep(5)
        

   
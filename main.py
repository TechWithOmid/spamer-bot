#!/usr/bin/env python3

import pyautogui
import time


f = open('script.txt', 'a')
num = int(input('how many time do you want to send: '))
spam_content = input('set your spam content: ')


def create_script(num):
    for i in range(num):
        f.write(f'{spam_content}\n')


script = open('script.txt', 'r')
def spammer(script):
    for word in script:
        pyautogui.typewrite(word)
        pyautogui.press('enter')



create_script(num)
f.close()

time.sleep(2)
spammer(script)

script.close()

print('====== Done ======')

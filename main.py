import pyautogui
import time


f = open('script.txt', 'a')
num = int(input('how many time do you want to send: '))


def create_script(num):
    for i in range(num):
        f.write('Fuck You Milad\n')

script = open('script.txt', 'r')

def spammer(script):
    for word in script:
        pyautogui.typewrite(word)
        pyautogui.press('enter')



create_script(num)
time.sleep(5)
spammer(script)

f.close()

script.close()

print('====== Done ======')

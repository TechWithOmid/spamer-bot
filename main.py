import pyautogui
import os
import time


class Spamer:

    sleep_time = 0
    spam_count = ''
    spam_content = ''
    current_path = dir_path = os.path.dirname(os.path.realpath(__file__))
    status = False  # True or False => define in check for script

    def check_for_script(self):
        for root, dir, files in os.walk(self.current_path):
            if 'script.txt' in files:
                self.status = True

        return self.status

    def create_script(self, count, content, spam_script):
        for i in range(count):
            spam_script.write(f'{content}\n')

    def spammer(self, spam_script):
        time.sleep(self.sleep_time)
        print('yes func')
        for word in spam_script:
            print('yes loop')
            pyautogui.typewrite(word)
            pyautogui.press('enter')


s = Spamer()
s.check_for_script()


if s.status:
    user_spam_option = input(
        'Do you want to use your last spam content(y/n): ')
    s.sleep_time = int(input('set sleep timer(sec): '))


    if user_spam_option == 'y':
        with open('script.txt', 'r') as spam_file:
            s.spammer(spam_file)

    elif user_spam_option == 'n':
        # delete script.txt 
        os.remove('script.txt')

        # create and add new data to script.txt
        s.spam_count = int(input('set the spam count: '))
        s.spam_content = input('set your spam content: ')
        with open('script.txt', 'a') as spam_source:
            s.create_script(s.spam_count, s.spam_content, spam_source)

        # start spaming
        with open('script.txt', 'r') as spam_script:
            s.spammer(spam_script)
        


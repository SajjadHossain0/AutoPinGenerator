import pyautogui
import time
import random
while True:
    number = "1234567890"
    length = 8
    password = "".join(random.sample(number, length))
    # print(password)
    time.sleep(1)
    pyautogui.typewrite(password)
    time.sleep(1)
    pyautogui.press('enter')



import pyautogui
from time import sleep
import random

sleep(2)

pyautogui.PAUSE = 0.5
pyautogui.FAILSAFE = True


# print(pyautogui.position())


def remove_post(x, y):
    pyautogui.click(x, y)

    # remove post
    try:
        x, y = pyautogui.locateCenterOnScreen('screen/2.png', confidence=0.8)
        pyautogui.click(x, y)
        sleep(random.randint(1, 3))
        # approve
        x, y = pyautogui.locateCenterOnScreen('screen/3.png', confidence=0.8)
        pyautogui.click(x, y)
    except TypeError:
        pyautogui.moveTo(x=1090, y=925, duration=0.1)
        pyautogui.scroll(-150)
    try:
        x, y = pyautogui.locateCenterOnScreen('screen/2.png', confidence=0.8)
        pyautogui.click(x, y)
        sleep(random.randint(1, 3))
        x, y = pyautogui.locateCenterOnScreen('screen/3.png', confidence=0.8)
        pyautogui.click(x, y)
    except TypeError:
        pyautogui.click(1430, 530)
        pyautogui.scroll(-200)


while True:
    try:
        sleep(random.randint(1, 3))
        x, y = pyautogui.locateCenterOnScreen('screen/1.png', confidence=0.8)
        remove_post(x, y)
        sleep(random.randint(1, 3))
    except TypeError:
        pyautogui.scroll(-300)

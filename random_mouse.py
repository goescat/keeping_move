import pyautogui
import random
import time

while True:
    width, height = pyautogui.size()

    x = random.randint(0, width - 1)
    y = random.randint(0, height - 1)

    print("move to:", x, y)

    pyautogui.moveTo(x, y, duration=1)

    time.sleep(random.randint(1, 3))
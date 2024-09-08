import pyautogui
import time

time.sleep(2)
while True:
    x, y = pyautogui.position()
    pixel = pyautogui.pixel(x, y)
    print(pixel)

    # in morning
    if pixel == (83, 83, 83):
        pyautogui.press("space")

    # in night
    elif pixel == (172, 172, 172):
        pyautogui.press("space")

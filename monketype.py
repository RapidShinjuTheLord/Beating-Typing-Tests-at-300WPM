import time
from PIL import Image
import pyautogui
import random
#import pytesseract
import easyocr

#note: safari window is positioned topleft corner (0,0) with 960 height, 832 width by screenshot coords

time.sleep(1)
reader = easyocr.Reader(['en'])
time.sleep(1)
pyautogui.keyDown("command")
pyautogui.keyDown("space")
pyautogui.keyUp("command")
pyautogui.keyUp("Space")
pyautogui.write("safari")
pyautogui.press("enter")
time.sleep(1)
pyautogui.write("https://monkeytype.com/")
pyautogui.press("enter")
time.sleep(8)
im = pyautogui.screenshot('screenshots/screenshot.png', region = (46,700, 1794, 260))


inittime = time.time()
while (time.time() - inittime) < 32:
        
    imagedir = 'screenshots/screenshot.png'
    result = reader.readtext(imagedir, detail=0, paragraph = True)
    string = ""
    for word in result:
        string += word + " "
    print(string)
    pyautogui.write(result[0] + ' ')
    time.sleep(0.2)
    im = pyautogui.screenshot('screenshots/screenshot.png', region = (50,780, 1790, 180))


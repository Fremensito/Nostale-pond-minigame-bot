from PIL import Image, ImageGrab
import numpy as np
import cv2
import pygetwindow as gw
import pyautogui
import pygetwindow

up = Image.open('up.png')
down = Image.open('down.png')
left = Image.open('left.png')
right = Image.open('right.png')
up = np.array(up.convert('L'))
down = np.array(down.convert('L'))
left = np.array(left.convert('L'))
right = np.array(right.convert('L'))

window = pygetwindow.getWindowsWithTitle("Nostale")[0]

def upFoo():
    result = cv2.matchTemplate(screenshot, up, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # Check if the reference image is found in the screenshot
    if max_val >= 0.8:  # You can adjust the threshold value for matching accuracy
        print("up")
        pyautogui.press("up")
        
def downFoo():
    result = cv2.matchTemplate(screenshot, down, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # Check if the reference image is found in the screenshot
    if max_val >= 0.8:  # You can adjust the threshold value for matching accuracy
        print("down")
        pyautogui.press("down")

def leftFoo():
    result = cv2.matchTemplate(screenshot, left, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # Check if the reference image is found in the screenshot
    if max_val >= 0.8:  # You can adjust the threshold value for matching accuracy
        print("left")
        pyautogui.press("left")

def rightFoo():
    result = cv2.matchTemplate(screenshot, right, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # Check if the reference image is found in the screenshot
    if max_val >= 0.8:  # You can adjust the threshold value for matching accuracy
        print("right")
        pyautogui.press("right")

while True:

    x = window.left + 297   # x-coordinate of the top-left corner of the ROI
    y = window.top + 220  # y-coordinate of the top-left corner of the ROI
    width = 991 - 297   # width of the ROI
    height = 810 - 220   # height of the ROI
    screenshot = pyautogui.screenshot(region=(x, y, width, height))
    screenshot = np.array(screenshot)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

    upFoo()
    downFoo()
    rightFoo()
    leftFoo()


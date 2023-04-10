from PIL import Image, ImageGrab
import numpy as np
import cv2
import pygetwindow as gw
import pyautogui
import pygetwindow


leftPond = Image.open('leftPond.png')
leftPond = np.array(leftPond.convert('L'))
downPond = Image.open('downPond.png')
downPond = np.array(downPond.convert('L'))
upPond = Image.open('upPond.png')
upPond = np.array(upPond.convert('L'))
rightPond = Image.open('rightPond.png')
rightPond = np.array(rightPond.convert('L'))


window = pygetwindow.getWindowsWithTitle("Nostale")[0]


def compareLeftPond():
    x = window.left + 425   # x-coordinate of the top-left corner of the ROI
    y = window.top + 453  # y-coordinate of the top-left corner of the ROI
    width = 522 - 425   # width of the ROI
    height = 535 - 453   # height of the ROI
    screenshot = pyautogui.screenshot(region=(x, y, width, height))
    screenshot = np.array(screenshot)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(screenshot, leftPond, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if max_val >= 0.94:  # You can adjust the threshold value for matching accuracy
        print("left")
        pyautogui.press("left")

def compareDownPond():
    x = window.left + 563   # x-coordinate of the top-left corner of the ROI
    y = window.top + 526  # y-coordinate of the top-left corner of the ROI
    width = 682 - 563   # width of the ROI
    height = 609 - 526   # height of the ROI
    screenshot = pyautogui.screenshot(region=(x, y, width, height))
    screenshot = np.array(screenshot)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(screenshot, downPond, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if max_val >= 0.96:  # You can adjust the threshold value for matching accuracy
        print("down")
        pyautogui.press("down")

def compareUpPond():
    x = window.left + 607   # x-coordinate of the top-left corner of the ROI
    y = window.top + 406  # y-coordinate of the top-left corner of the ROI
    width = 719 - 607   # width of the ROI
    height = 474 - 406   # height of the ROI
    screenshot = pyautogui.screenshot(region=(x, y, width, height))
    screenshot = np.array(screenshot)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(screenshot, upPond, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if max_val >= 0.96:  # You can adjust the threshold value for matching accuracy
        print("up")
        pyautogui.press("up")

def compareRightPond():
    x = window.left + 760   # x-coordinate of the top-left corner of the ROI
    y = window.top + 468  # y-coordinate of the top-left corner of the ROI
    width = 881 - 760   # width of the ROI
    height = 530 - 468   # height of the ROI
    screenshot = pyautogui.screenshot(region=(x, y, width, height))
    screenshot = np.array(screenshot)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(screenshot, rightPond, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if max_val >= 0.938:  # You can adjust the threshold value for matching accuracy
        print("right")
        pyautogui.press("right")

while True:
    compareLeftPond()
    compareDownPond()
    compareUpPond()
    compareRightPond()




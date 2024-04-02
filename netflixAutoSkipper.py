import numpy as np
import cv2
import pyautogui as pag
import time

img_path = r'C:\Users\brend\OneDrive - Middlesex University\Documents\GitHub\Netflix-IntroOST-Auto_Skipper\netflix_ss.png'
template_path = r'C:\Users\brend\OneDrive - Middlesex University\Documents\GitHub\Netflix-IntroOST-Auto_Skipper\skipIntroButton.png'
img = cv2.imread(img_path, 0)
template = cv2.imread(template_path, 0)
height, width = template.shape

methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR]

for method in methods:
    img2 = img.copy()
    result = cv2.matchTemplate(img2, template, method)
    min_val ,max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc

    bottom_right = (location[0] + width, location[1] + height)
    
    cv2.rectangle(img2, location, bottom_right, 0, 5)
    # cv2.imshow("Method", img2)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

time.sleep(2)
x, y = location
print(x,y)
pag.moveTo(x + 10, y + 10)
pag.click()
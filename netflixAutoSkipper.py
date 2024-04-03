import numpy as np
import cv2
import pyautogui 
import time
import pytesseract

# Set the path to tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

while True:
    img = pyautogui.screenshot()
    frame = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2GRAY)

    # Apply OCR to the screenshot
    text = pytesseract.image_to_string(frame)

    # Check if "Skip" text is present
    if "Skip Intro" in text:
        print("Skip button found!")
        # Add your code here to handle the skip button

# import numpy as np
# import cv2
# import pyautogui 
# import time
# import pytesseract

# #NEEDS to have an realtime update from Comptuer screen! use pyautogui.screenshot()
# template_path = r'C:\Users\brend\OneDrive - Middlesex University\Documents\GitHub\Netflix-IntroOST-Auto_Skipper\skipIntroButton.png'

# while True:
#     img = pyautogui.screenshot()
#     frame = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2GRAY)
#     template = cv2.imread(template_path, 0)
#     height, width = template.shape

#     frame = cv2.GaussianBlur(frame, (5, 5), 0)
#     template = cv2.GaussianBlur(template, (5, 5), 0)
#     img2 = frame.copy()
#     result = cv2.matchTemplate(img2, template, cv2.TM_CCOEFF_NORMED)
#     min_val ,max_val, min_loc, max_loc = cv2.minMaxLoc(result)
#     top_left = min_loc
#     bottom_right = (top_left[0] + width, top_left[1] + height)
#     print('top left' , top_left)
#     print('bot_right' , bottom_right)
#     cv2.rectangle(img2, top_left, bottom_right, 0, 5)
#     cv2.imshow("Results", img2)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

#     if min_loc:
#         time.sleep(2)
#         x = (top_left[0] + bottom_right[0])/2
#         y = (top_left[1] + bottom_right[1])/2
#         print(x,y)
#         pyautogui.moveTo(x , y, 2)
#         pyautogui.click()
import pyautogui 
import time
import cv2
import numpy as np

def find_skip_button(screen_width, screen_height):
    # Buffer time for user to switch to browser window
    time.sleep(3)

    path = r"c:\Users\brend\OneDrive - Middlesex University\Documents\GitHub\Netflix-IntroOST-Auto_Skipper\netflix_ss.png"
    # Load skip button image
    skip_button = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    cv2.imshow('image',skip_button)
    cv2.waitKey(0)

    # Get screen resolution
    screen = np.array(pyautogui.screenshot())
    gray_screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    cv2.imshow('screen',gray_screen)
    cv2.waitKey(0)

    # Perform template matching
    skip_match = cv2.matchTemplate(gray_screen, skip_button, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(skip_match)

    # Matching score threshold
    th = 0.9
    if max_val >= th:
        button_x, button_y = max_loc[0] + skip_button.shape[1] // 2, max_loc[1] + skip_button.shape[0] // 2
        return button_x, button_y
    else:
        return None

def skip_button_clicker(screen_width, screen_height):
    skip_button_coordinates = find_skip_button(screen_width, screen_height)
    if skip_button_coordinates:
        print('Skip button found')
        # Check if coordinates are within screen bounds
        if 0 <= skip_button_coordinates[0] <= screen_width and 0 <= skip_button_coordinates[1] <= screen_height:
            pyautogui.moveTo(skip_button_coordinates)
            pyautogui.click()
        else:
            print("Skip button coordinates out of bounds.")
    else:
        print("Skip button not found.")

if __name__ == "__main__":
    # Get screen resolution
    screen = np.array(pyautogui.screenshot())
    gray_screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    screen_height, screen_width = gray_screen.shape[::-1]  # Reverse shape for OpenCV
    
    while True:
        skip_button_clicker(screen_width, screen_height)
        time.sleep(5)  # Wait for a few seconds before checking again



# import pyautogui 
# import time
# import cv2
# import numpy as np

# def find_skip_button():
#     # Buffer time for user to switch to browser window
#     time.sleep(5)

#     path = r"c:\Users\brend\OneDrive - Middlesex University\Documents\GitHub\Netflix-IntroOST-Auto_Skipper\netflix_ss.png"
#     # Load skip button image
#     skip_button = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

#     # Perform template matching
#     skip_match = cv2.matchTemplate(gray_screen, skip_button, cv2.TM_CCOEFF_NORMED)
#     min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(skip_match)

#     # Matching score threshold
#     th = 0.9
#     if max_val >= th:
#         button_x, button_y = max_loc[0] + skip_button.shape[1] // 2, max_loc[1] + skip_button.shape[0] // 2
#         return button_x, button_y
#     else:
#         return None

# def skip_button_clicker():
#     skip_button_coordinates = find_skip_button()
#     if skip_button_coordinates:
#         # Check if coordinates are within screen bounds
#         if 0 <= skip_button_coordinates[0] <= screen_width and 0 <= skip_button_coordinates[1] <= screen_height:
#             pyautogui.moveTo(skip_button_coordinates)
#             pyautogui.click()
#         else:
#             print("Skip button coordinates out of bounds.")
#     else:
#         print("Skip button not found.")

# # if __name__ == "__main__":
# while True:

#     # Get screen resolution
#     screen = np.array(pyautogui.screenshot())
#     gray_screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
#     screen_height, screen_width = gray_screen.shape[::-1]  # Reverse shape for OpenCV
#     skip_button_clicker()


# import pyautogui 
# import time
# import cv2
# import numpy as np

# def find_skip_button():
#     #Buffer time for user to have time to change to browser
#     time.sleep(5)

#     #Load skip button image
#     skip_button =cv2.imread('netlix_ss.png', cv2.IMREAD_GRAYSCALE)

#     #Get screen resolution
#     screen = np.array(pyautogui.screenshot())
#     gray_screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
#     screen_height, screen_width = gray_screen.shape

#     #Perform template matching
#     skip_match = cv2.matchTemplate(gray_screen, skip_button, cv2.TM_CCOEFF_NORMED)
#     min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(skip_match)

#     # Matching score threshold
#     th = 0.9
#     if max_val >= th:
#         button_x, button_y = max_loc[0] + skip_button.shape[1] // 2, max_loc[1] + skip_button.shape[0] // 2
#         return button_x, button_y
#     else:
#         return None

# def skip_button_clicker():
#     skip_button_coordinates = find_skip_button()
#     if skip_button_coordinates:
#         pyautogui.moveTo(skip_button_coordinates)
#         pyautogui.click()
#     else:
#         pass  

# if __name__ == "__main__":
#     skip_button_clicker()

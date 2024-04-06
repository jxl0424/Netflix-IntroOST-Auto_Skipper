import time
import pyautogui
import numpy as np
import cv2

# Continuos loop for see if there are any Skip Recap/ Skip Intro or Next Episode button
while True:
    time.sleep(1)
# Get a screenshot of the screen
    img = pyautogui.screenshot()
    img = np.asarray(img.convert(mode = 'L'))
    path_intro_template = r'C:\Users\brend\OneDrive - Middlesex University\Documents\GitHub\Netflix-IntroOST-Auto_Skipper\skipIntro1.png'
    path_recap_template = r'C:\Users\brend\OneDrive - Middlesex University\Documents\GitHub\Netflix-IntroOST-Auto_Skipper\skipRecap.png'
    path_next_episode_template = r'C:\Users\brend\OneDrive - Middlesex University\Documents\GitHub\Netflix-IntroOST-Auto_Skipper\nextEpisode.png'
    intro_template = cv2.imread(path_intro_template, 0)
    recap_template = cv2.imread(path_recap_template, 0)
    episode_template = cv2.imread(path_next_episode_template, 0)

# Set a threshold to get a better result
    threshold = 0.8

# Check for skip intro  
    res = cv2.matchTemplate(img, intro_template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)

# Check if intro template is matched
    if loc[0].size != 0:
        x = loc[1]
        y = loc[0]
# Click on the location of the button
        pyautogui.click(x, y)
        continue # continue loop from start without further execution of the loop

# Check for skip recap
    res = cv2.matchTemplate(img, recap_template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)

# Check if recap template is matched
    if loc[0].size != 0:
        x = loc[1]
        y = loc[0]
# Click on the location of the button
        pyautogui.click(x, y)
        continue # continue loop from start without further execution of the loop

# Check for next episode
    res = cv2.matchTemplate(img, episode_template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)

# Check if episode template is matched
    if loc[0].size != 0:
        x = loc[1]
        y = loc[0]       
# Click on the location of the button
        pyautogui.click(x + 5, y + 5)
        continue # continue loop from start without further execution of the loop


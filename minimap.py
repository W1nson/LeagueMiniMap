from concurrent.futures import process
import cv2 
from PIL import ImageGrab
import numpy as np
import time
import pyautogui
import ctypes


user32 = ctypes.windll.user32
screensize =0,0, user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
bottom_right = user32.GetSystemMetrics(0) -400, user32.GetSystemMetrics(1) - 450, user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)-50
print(screensize) 
print(bottom_right[0], bottom_right[1], bottom_right[2], bottom_right[3])

center = (bottom_right[2]-bottom_right[0])//2 + 60,  (bottom_right[3]-bottom_right[1]) //2 + 70
# center = bottom_right[0], bottom_right[1]
print(center) 
radius = 30
color = (255, 0, 0)
def process_img(original_image):
    processed_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    # processed_img = cv2.Canny(processed_img, threshold1=200, threshold2=300)
    processed_img = cv2.circle(processed_img, center, radius, color, thickness=2)
    return processed_img



last_time = time.time()
while(True):
    screen = np.array(ImageGrab.grab(bbox=bottom_right))
    new_screen = process_img(screen)
    print('Loop took {} seconds'.format(time.time()-last_time))
    last_time = time.time()
    cv2.imshow('window', new_screen)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break 
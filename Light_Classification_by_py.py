import cv2
import numpy as np


def detect_color(image):
    
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)


    
    lower_red = np.array([0,120,70])
    upper_red = np.array([10,255,255])
    lower_yellow = np.array([20,100,100])
    upper_yellow = np.array([30,255,255])
    lower_green = np.array([50,100,100])
    upper_green = np.array([70,255,255])


    
    red_mask = cv2.inRange(hsv, lower_red, upper_red)
    yellow_mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    green_mask = cv2.inRange(hsv, lower_green, upper_green)


   
    red_area = np.sum(red_mask)
    yellow_area = np.sum(yellow_mask)
    green_area = np.sum(green_mask)


    if red_area > yellow_area and red_area > green_area:
        return "RED"
    elif yellow_area > red_area and yellow_area > green_area:
        return "YELLOW"
    elif green_area > red_area and green_area > yellow_area:
        return "GREEN"
    else:
        return "UNKNOWN"




img = cv2.imread("/content/traffic-light1.jpg")




color = detect_color(img)




print("The traffic light is:", color)

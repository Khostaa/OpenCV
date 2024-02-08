import cv2 as cv
import numpy as np 

#color format (b, g, r)

blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Blank', blank)

img = cv.imread('Resources/Photos/cat.jpg')
cv.imshow('Cat', img)

# 1. Paint the image a certain colour
# [ range of pixels to color inside brackets of blank]
blank[200: 300, 300:400] = 0, 255, 0
cv.imshow('Green', blank)

# 2. Draw a Rectangle
# temp: cv.rectangle (img, pt1, pt2, color, thickness=None, lineType=None, shift=None, /)
cv.rectangle(blank,(0, 0),(250, 500),(0,255,0),thickness = cv.FILLED) # Green rectangle with color filled
# cv.rectangle(blank,(0, 0),(250, 250),(0,255,0),thickness = 2) # Green rectangle with thickness=2
# cv.rectangle(blank,(0, 0),(blank.shape[1]//2, blank.shape[0]//2),(0,255,0),thickness = 1)
cv.imshow('Rectangle', blank)

# 3. Draw a Circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40,  (0, 0, 255), thickness = 5)
cv.imshow('Circle', blank)

# 4. Draw a Line
cv.line(blank, (0,0), (250, 250), (255, 255, 255), thickness = 3)
cv.imshow("Line", blank)

# 5. Write a Text in Image
cv.putText(blank, "Hello World!",  (50, 75), cv.FONT_HERSHEY_SIMPLEX , 1, (255, 0, 0))
cv.imshow('Text', blank)
cv.waitKey(0)


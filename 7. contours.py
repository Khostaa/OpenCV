import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/cats.jpg')

cv.imshow('Cats', img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

# CONVERTING IMAGE TO GRAYSCALE
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Applying Blur
blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)


#first use canny then find countours using that

# Edge Detection
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

# finding countour
# thresholding means binarzing the image i.e, 0 or 1.
# if pixel is below 125 - it's going to be set to 0 (black)
# if pixel is above 125 - it's set to white (255)

# ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
# cv.imshow("Thresh", thresh)



# anoter way to find contours
#cv.RETR_TREE - for all the hierarhical contours
#cv.RETR_EXTERNAL - for external contours
#cv.RETR_LIST - for all contours in the list

##   contour approximation method
#cv.CHAIN_APPROX_NONE - it is doing nothing in this case - gets all the coordinates/point
#cv.CHAIN_APPROX_SIMPLE - removes the redundant points and makes a polygon or line from them
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)

# displaying no. of contours
print(f'No. of Contours: {len(contours)}')

#drawing contours
cv.drawContours(blank, contours, -1, (0, 0, 255), 1)
cv.imshow('Contours Drawn', blank)
cv.waitKey(0)
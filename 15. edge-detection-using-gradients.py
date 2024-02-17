import cv2 as cv
import numpy as np

#uint8 - image specific data type

img = cv.imread('Resources/Photos/park.jpg')
cv.imshow('Park', img)

# Gradients and edges detection are completely diff. things from mathamatical point of view

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# To detect edge using
# Laplacian Method
lap = cv.Laplacian(gray, cv.CV_64F)
# images itself cannot have -ve pixel values. so we essentially compute absolute values of that image
# so that all the pixel values of image are converted to absolute values and then we convert it to uint8
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)

# Sobel
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0) # Take only x derivative
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1) # Take only y derivative
combined_sobel = cv.bitwise_or(sobelx, sobely)

cv.imshow('Sobel X', sobelx)
cv.imshow('Sobel Y', sobely)
cv.imshow('Combined Sobel', combined_sobel)

# canny uses more advanced version of sobel
canny = cv.Canny(gray, 150, 175)
cv.imshow('Canny',canny)

cv.waitKey(0)


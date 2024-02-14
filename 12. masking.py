import cv2 as cv 
import numpy as np

img = cv.imread('Resources/Photos/cats.jpg')
cv.imshow("Cat", img)

blank = np.zeros(img.shape[:2], dtype = 'uint8')
cv.imshow('Blank Image', blank)

# Creating mask canvas
circle = cv.circle(blank, (img.shape[1]//2 + 45, img.shape[0]//2), 100, 255, -1)
cv.imshow('Mask', circle)

rectangle = cv.rectangle(blank, (30, 30), (370, 370), 255, -1)

weird_shape = cv.bitwise_and(circle, rectangle)
cv.imshow('Weird Shape', weird_shape)

## For rectangular Masking canvas
# maskrec = cv.rectangle(blank, (img.shape[1]//2, img.shape[0]//2),(img.shape[1]//2 + 200, img.shape[0]//2 + 100), 255, -1)
# cv.imshow('Mask2', maskrec)

# applying the mask
masked = cv.bitwise_and(img, img, mask= weird_shape)
cv.imshow('Masked Image', masked)

## Applying rectangular masking to img.
# masked2 = cv.bitwise_and(img, img, mask=maskrec)
# cv.imshow('Masked Image 2', masked2)

cv.waitKey(0)
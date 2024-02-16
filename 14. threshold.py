import cv2 as cv

img = cv.imread('Resources/Photos/cats.jpg')
cv.imshow("Cat", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# Simple Thresholding
# IF ABOVE 150 SETS IT TO 255
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('Simple Thresholded', thresh)

# sets value above 150 to 0 and rest to 255 i.e, inversing the values
threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simple Thresholded Inverse', thresh_inv)

# Adaptive Threshoding
# ADAPTIVE_THRESH_GAUSSIAN_C or ADAPTIVE_THRESH_MEAN_C
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 1)
cv.imshow('Adaptive Thresholding', adaptive_thresh)

cv.waitKey(0)

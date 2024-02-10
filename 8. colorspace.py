## OpenCV uses BGR color space instead of RGB

import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Resources\Photos\park.jpg')
cv.imshow('park', img)

plt.imshow(img)
plt.show()

#BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("HSV", hsv)

# BGR to LAB/ L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

# BGR to RGT
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb) # RGB is displayed inversely as OPENCV support BGR

plt.imshow(rgb) # RGB is shown as it in matplotlib
plt.show()

# HSV to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('HSV --> BGR', hsv_bgr)

# LAB to BGR
lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow('LAB --> BGR', lab_bgr)


# There is no direct way to convert grayscale to lab. 
#for that, grayscale needs to be converted to bgr and then bgr to lab.
cv.waitKey(0)
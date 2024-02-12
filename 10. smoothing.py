import cv2 as cv

img = cv.imread('Resources/Photos/cats.jpg', 1)
cv.imshow("Cats", img)

# Averaging
# computes average of surrounding pixels to compute blur density for middle pixel
# (3, 3) is kernel/window size. greater the no., higher the blur
average = cv.blur(img, (7,7))
cv.imshow('Average Blur', average)

# Gaussian Blur
# less and more natural blur than averaging
gauss = cv.GaussianBlur(img, (7,7), 0)
cv.imshow('Gaussian Blur', gauss)

# Median Blur
# more effective in reducing noise in image
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median)

# Bilateral Blur
bilateral = cv.bilateralFilter(img, 5, 35, 25)
cv.imshow('Bilateral Filtering', bilateral)


cv.waitKey(0)

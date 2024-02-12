import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/park.jpg')
cv.imshow('Park', img)

blank = np.zeros(img.shape[:2], dtype='uint8')


# Splitting color channels of image 'img'
b, g, r = cv.split(img)

# Applying merge and passing on values so as to display respective color channel only
blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

# in output lighter distribution represents greater presence of color in image
cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)

# printing the shape and color channels of image
print(img.shape) # 3 is color channel in o/p
print(b.shape)
print(g.shape)
print(r.shape)

# Merging the separated color channels back into a single channel image
merged = cv.merge([b, g, r])
cv.imshow('Merge BGR', merged)

cv.waitKey(0)
import cv2 as cv
import numpy as np

img = cv.imread("Resources/Photos/park.jpg")
cv.imshow("park", img)

# Translation
# x,y - no. of pixels to shift along x or y axis resp.
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])   #  Create a matrix for translation transformation
    dimensions = (img.shape[1], img.shape[0]) # (width, height)
    return cv.warpAffine(img, transMat, dimensions)

# -x --> Left
# -y --> Up
# x --> Right
# y --> Down

# translated = translate(img, 100, 100)
translated = translate (img, -100, 200)
cv.imshow('Translated', translated)

# Rotation
def rotate (img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated45 = rotate( img, 45) # 45 is rotation angle here
cv.imshow('Rotated', rotated45)

rotated25 = rotate(rotated45, -45) # rotated  again by -45 degree
cv.imshow('Rotated', rotated25)

# Resize
resized = cv.resize(img, (500, 500), interpolation = cv.INTER_CUBIC)
cv.imshow('Resized', resized)

#Flipping
flip = cv.flip(img, -1)  # -1 for flippig, can be changed to other values
cv.imshow('Flip', flip)

# Cropping
cropped = img[50:200, 200:400] 
cv.imshow("Cropped", cropped)

cv.waitKey(0)

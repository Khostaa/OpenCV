import cv2 as cv

img = cv.imread('Resources/Photos/park.jpg')
cv.imshow("Original", img)

# converting to grayscale
gray =  cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# Applying Blur
blur = cv.GaussianBlur(img, (1,7), cv.BORDER_DEFAULT)
cv.imshow("Blur", blur)

# Edge Detection/Cascade
# 'blur' is passed to function for less edge
canny = cv.Canny(blur, 125, 175) 
cv.imshow('Canny Edges', canny)

# Dilating the image
dilated = cv.dilate(canny, (7,7), iterations = 3)
cv.imshow('Dilated', dilated)

# Eroding (gettting back org. img. from dialted image)
eroded = cv.erode(dilated, (7,7),iterations=3)
cv.imshow( "Eroded", eroded )

# Resize
# interpolation : cv.INNER_AREA for decreasing image dimenstions than org. image
# cv.INTER_LINEAR/CUBIC for enlarging image
resized = cv.resize(img, (500,500), interpolation = cv.INTER_AREA)
cv.imshow('Resized', resized)

# Cropping
cropped = img[50:200, 200:400] 
cv.imshow("Cropped", cropped)
cv.waitKey(0)
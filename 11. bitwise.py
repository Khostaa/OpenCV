import cv2 as cv
import numpy as np

blank = np.zeros((400, 400), dtype = 'uint8')

# drawing rectangle using blank variable
rectangle = cv.rectangle(blank.copy(), (30, 30), (370,  370), 255, -1)

circle = cv.circle(blank.copy(), (200, 200), 200, 255, -1)

cv.imshow('Rectangle', rectangle)
cv.imshow('Circle', circle)

# bitwise AND --> intersecting regions
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow('Bitwise And', bitwise_and)

#bitwise OR --> non-intersecting and intersecting regions
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow("Bitwise OR", bitwise_or)

#bitwise XOR --> non-intersecting regions
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('Bitwise XOR', bitwise_xor)

#bitwise AND
bitwise_not = cv.bitwise_not(rectangle)
cv.imshow( "Bitwise NOT", bitwise_not)

cv.waitKey(0)
import cv2 as cv

#  img = cv.imread('Resources/Photos/lady.jpg')
img = cv.imread('Resources/Photos/group 1.jpg')
cv.imshow('Person', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray person', gray)

# passing path to xml file to cascade classifier
haar_cascade = cv.CascadeClassifier('haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors= 1)

print(f'Number of faces found = {len(faces_rect)}')

for (x, y, w, h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), thickness = 2)

cv.imshow('Detected Faces', img) 


cv.waitKey(0)
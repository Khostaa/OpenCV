import cv2 as cv

capture = cv.VideoCapture('Resources/Videos/dog.mp4')  # Create a VideoCapture object to capture video from camera

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF == ord ('d'):
        break

capture.release()
cv.destroyAllWindows()
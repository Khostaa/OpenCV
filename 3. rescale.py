import cv2 as cv

def rescaleFrame(frame, scale = 0.75):
    # works for images, videos and live videos
    width = int(frame.shape[1] * scale) #frame.shape is org. width & height of frame
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

# cv.resize function resizes frame using cv.INTER_AREA interpolation method,
# which is suitable for shrinking images. It does not work well when reducing size.
    return cv.resize(frame, dimensions, interpolation= cv.INTER_AREA)

def changeRes(width, height):
    # Only works for live videos
    capture.set(3, width)
    capture.set(4, height)
# Reading image
img = cv.imread('Resources/Photos/cat.jpg') #reads an image file from the given path and stores it in img var.

# Rescaling the image
resized_image = rescaleFrame(img) #calls and passes img to rescaleFrame function.

# creast window named 'Image' and displays ' resized_image' variable on it.
cv.imshow('Image', resized_image)

# READING VIDEOS    
capture = cv.VideoCapture ('Resources/Videos/dog.mp4') #reads vide from path and stores it in capture variable.

# To read video from webcam: cv.VideoCapture(0) similarly, 1, 2, 3 ,.. for rest of the cameras connected to pc resp.
while True:
    # reads next frame form capture object and stores it in frame variable.
    # isTrue is boolean var. that indicates whether the frame was successfully read or not.
    isTrue, frame = capture.read()

    # call rescaleFrame function and passes frame to the function.
    frame_resized = rescaleFrame(frame)

    # creates window named "Video" with original size
    cv.imshow('Video', frame)

    #creates window name "Video Resized" with resized frame
    cv.imshow('Video Resized', frame_resized)

    #checks if any key is pressed by user. If yes then break the loop.
    if cv.waitKey(20) & 0xFF == ord ('d'): #closes window when 'd' is pressed
        break

capture.release() # releases the caputre object and frees the resources.
cv.destroyAllWindows() #closes all the windows created by cv.imshow function.
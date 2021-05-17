import cv2 as cv
import numpy as np

pic1 = cv.imread('pic1.jpg')
pic2 = cv.imread('pic2.jpg')
pic3 = cv.imread('pic3.jpg')

cv.imshow('pic1', pic1)
cv.imshow('pic2', pic2)
cv.imshow('pic3', pic3)
cv.waitKey(0)

vid1 = cv.VideoCapture('vid1.mp4')

while True:
    isTrue, frame = vid1.read()
    if isTrue:
        cv.imshow('Video', frame)
    else:
        print('empty frame')
        exit(1)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

vid1.release()
cv.destroyAllWindows()
    
cv.waitKey(0)

def rescaleFrame(frame, scale = 0.5):
    
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA) #will talk more about this later

img = cv.imread('pic1.jpg')

img_rescaled = rescaleFrame(img)

cv.imshow('Dog', img)
cv.imshow('Dog_rescaled', img_rescaled)


cv.waitKey(0)

def rescaleFrame(frame, scale = 0.5):
    
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA) #will talk more about this later


capture = cv.VideoCapture('vid1.mp4')


while True:
    isTrue, frame = capture.read()
    
    
    if frame is not None:
        frame_rescaled = rescaleFrame(frame)
        cv.imshow('Video', frame)
        cv.imshow('Video_rescaled', frame_rescaled)
    else:
        print('empty frame')
        exit(1)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
    
cv.waitKey(0)

center = (pic2.shape[0]//2, pic2.shape[1]//2)
radius = min(pic2.shape[0]//4, pic2.shape[1]//4)

cv.circle(pic2, center, radius, (0, 0, 255), thickness = -1)
cv.imshow('Circle', pic2)
pic2 = cv.imread('pic2.jpg')
cv.imshow('Orig', pic2)
cv.waitKey(0)

center = (pic2.shape[0]//2, pic2.shape[1]//2)
radius = min(pic2.shape[0]//4, pic2.shape[1]//4)

pic2 = cv.imread('pic2.jpg')
cv.rectangle(pic2, (pic2.shape[1]//4, pic2.shape[0]//4), (pic2.shape[1]//2, pic2.shape[0]//2), (0, 128, 255), thickness = cv.FILLED)
cv.imshow('Rectangle', pic2)
pic2 = cv.imread('pic2.jpg')
cv.imshow('Orig', pic2)
cv.waitKey(0)

cv.line(pic3, (0, pic3.shape[1]), (pic3.shape[0], 0), (0, 255, 0))
cv.imshow('Line', pic3)
pic3 = cv.imread('pic3.jpg')
cv.imshow('Orig', pic3)
cv.waitKey(0)

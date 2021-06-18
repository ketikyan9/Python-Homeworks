import cv2 as cv
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

pic1 = cv.imread('pic1.jpg') 

# prob 1

gray = cv.cvtColor(pic1, cv.COLOR_BGR2GRAY)
gray_hist = cv.calcHist([gray], [0], None, [256], [0,256]) 
gray_hist = [i[0] for i in gray_hist]

mpl.use('tkagg')
x = np.arange(256)
plt.plot(x,gray_hist)
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')

plt.show()

# prob 2

colors = ('b', 'g', 'r')

for i, col in enumerate(colors):
    hist = cv.calcHist([pic1], [i], None, [256], [0,256]) 
    mpl.use('tkagg') #backend for using matplotlib with any shell
    x = np.arange(256)
    plt.plot(x,hist, color=col)
    plt.title('Color Histogram')
    plt.xlabel('Bins')
    plt.ylabel('# of pixels')

plt.show()

# prob 3

cv.imshow('pic1', pic1)

gray = cv.cvtColor(pic1, cv.COLOR_BGR2GRAY)

threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('simple threshold', thresh) 

adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 0)
cv.imshow('adaptive threshold', adaptive_thresh)

adaptive_thresh_gaussian = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 9)
cv.imshow('adaptive threshold gaussian', adaptive_thresh_gaussian) 

# prob 4

pic2 = cv.imread('pic2.jpg')
cv.imshow('pic2', pic2)

gray = cv.cvtColor(pic2, cv.COLOR_BGR2GRAY)

lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('laplacian', lap) 

canny = cv.Canny(gray, 150, 175)
cv.imshow('canny', canny) 

# Canny gives better results then laplacian method.

cv.waitKey(0)


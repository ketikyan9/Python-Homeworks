import cv2 as cv
import numpy as np

"""
# prob 1

pic1 = cv.imread('pic1.jpg')
cv.imshow('pic1', pic1)

pic_rgb = cv.cvtColor(pic1, cv.COLOR_BGR2RGB)
pic_hsv = cv.cvtColor(pic1, cv.COLOR_BGR2HSV)
pic_lab = cv.cvtColor(pic1, cv.COLOR_BGR2LAB)
pic_gray = cv.cvtColor(pic1, cv.COLOR_BGR2GRAY)

cv.imshow('rgb', pic_rgb)
cv.imshow('hsv', pic_hsv)
cv.imshow('lab', pic_lab)
cv.imshow('gray', pic_gray)

"""

"""
# prob 2

pic1 = cv.imread('pic1.jpg')
b, g, r = cv.split(pic1)

blank = np.zeros(pic1.shape[:2], dtype = 'uint8')
blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow('b gray', b)
cv.imshow('g gray', g)
cv.imshow('r gray', r)

cv.imshow('blue colored', blue)
cv.imshow('green colored', green)
cv.imshow('red colored', red)

"""

"""
# prob 3

pic2 = cv.imread('pic2.jpg')
cv.imshow('pic2', pic2)

average = cv.blur(pic2, (3,3))
bilateral1 = cv.bilateralFilter(pic2, 5, 15, 15)
bilateral2 = cv.bilateralFilter(pic2, 5, 15, 70)
bilateral3 = cv.bilateralFilter(pic2, 5, 70, 15)
bilateral4 = cv.bilateralFilter(pic2, 70, 15, 15)

cv.imshow('average blur', average)
cv.imshow('bilateral blur 1', bilateral1)
cv.imshow('bilateral blur 2', bilateral2)
cv.imshow('bilateral blur 3', bilateral3)
cv.imshow('bilateral blur 4', bilateral4)

# A bilateral blurring saves edges.
"""

"""
# prob 4 
pic2 = cv.imread('pic2.jpg')

blank = np.zeros(pic2.shape[:2], dtype = 'uint8')
mask = cv.circle(blank, (pic2.shape[1]//2, pic2.shape[0]//2), 70, (255, 0, 0), -1)

masked_image = cv.bitwise_and(pic2, pic2, mask=mask)

cv.imshow('original image', pic2) 
cv.imshow('result', masked_image)

"""

"""
# prob 5

blank = np.zeros(shape=(200,200))
rectangle = cv.rectangle(blank.copy(), (30, 30), (170, 170), 0.5, -1)
circle = cv.circle(blank.copy(), (100, 100), 85, 0.5, -1)

shape_1 = cv.bitwise_xor(rectangle, circle)
shape_2 = cv.bitwise_or(rectangle, circle)

blank = np.zeros(shape=(200,200, 3))
rectangle3 = cv.rectangle(blank.copy(), (30, 30), (170, 170), (199/255,21/255,133/255), -1)
circle3 = cv.circle(blank.copy(), (100, 100), 85, (199/255,21/255,133/255), -1)

shape_3 = cv.bitwise_xor(rectangle3, circle3)

cv.imshow('shape 1', shape_1)
cv.imshow('shape 2', shape_2)
cv.imshow('shape 3', shape_3)

"""

cv.waitKey(0)

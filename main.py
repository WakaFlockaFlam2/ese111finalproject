#! /usr/bin/python

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('dave.jpg',0)
img = cv2.medianBlur(img,15)
ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
nonzero = cv2.countNonZero(ret)
height, width = img.shape
print height
print width
blackPix = (height * width) - nonzero
numbugs = blackPix / 10000

titles = ['Original Image', 'Global Thresholding (v = 127)']
images = [img, th1]

for i in xrange(2):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
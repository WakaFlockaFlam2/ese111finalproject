#!/usr/bin/python

# Standard imports
import cv2
import numpy as np;
import os
import datetime
i = datetime.datetime.now()
# Read image
img_str = "training_imgs/w5.jpg"
im = cv2.imread(img_str, cv2.IMREAD_GRAYSCALE)
im = cv2.medianBlur(im,15)

# Setup SimpleBlobDetector parameters.
params = cv2.SimpleBlobDetector_Params()

# Change thresholds
params.minThreshold = 10
params.maxThreshold = 200


# Filter by Area.
params.filterByArea = True
params.minArea = 200

# Filter by Circularity
params.filterByCircularity = True
params.minCircularity = 0.1

# Filter by Convexity
params.filterByConvexity = True
params.minConvexity = 0.01
    
# Filter by Inertia
params.filterByInertia = True
params.minInertiaRatio = 0.01

# Create a detector with the parameters
ver = (cv2.__version__).split('.')
if int(ver[0]) < 3 :
	detector = cv2.SimpleBlobDetector(params)
else : 
	detector = cv2.SimpleBlobDetector_create(params)


# Detect blobs.
keypoints = detector.detect(im)

im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Show blobs
cv2.imshow("Keypoints", im_with_keypoints)
cv2.waitKey(0)
numBugs = len(keypoints)
print numBugs

os.system("ssh -i idamRevOne.pem ec2-user@ec2-54-144-59-153.compute-1.amazonaws.com 'bash adder.sh " +str(i.year) + "_"+str(i.month) + "_"+str(i.day) + "_" + str(i.hour) + "_" + str(i.minute)+ "_" + str(i.second)+" " +str(numBugs)+"'")
os.system("scp -i idamRevOne.pem "+ img_str +" ec2-user@ec2-54-144-59-153.compute-1.amazonaws.com:/var/www/html/images/"+str(i.year) + "_"+str(i.month) + "_"+str(i.day) + "_" + str(i.hour) + "_" + str(i.minute)+ "_" + str(i.second)+".jpg")
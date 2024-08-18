# import required libraries
import numpy as np
import cv2
from matplotlib import pyplot as plt

# read two input images
img1 = cv2.imread('/home/sukant/home_branch/cv_project/source/door_1.jpeg',0)
img2 = cv2.imread('/home/sukant/home_branch/cv_project/source/door_2.jpeg',0)

orb = cv2.ORB_create()
 
# find the keypoints 2with ORB
kp1 = orb.detect(img1,None)
 
# compute the descriptors with ORB
kp1, des1 = orb.compute(img1, kp1)
 
# find the keypoints with ORB
kp2 = orb.detect(img2,None)
 
# compute the descriptors with ORB
kp2, des2 = orb.compute(img2, kp2)

# FLANN parameters
FLANN_INDEX_KDTREE = 0
index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
search_params = dict(checks=50) # or pass empty dictionary

# apply FLANN based matcher with knn
flann = cv2.FlannBasedMatcher(index_params,search_params)
matches = flann.knnMatch(des1,des2,k=2)

# Need to draw only good matches, so create a mask
matchesMask = [[0,0] for i in range(len(matches))]

# ratio test as per Lowe's paper
for i,(m,n) in enumerate(matches):
   if m.distance < 0.1*n.distance:
      matchesMask[i]=[1,0]
draw_params = dict(matchColor = (0,255,0),singlePointColor = (255,0,0),matchesMask = matchesMask,flags = 0)
img3 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,matches,None,**draw_params)
plt.imshow(img3),plt.show()
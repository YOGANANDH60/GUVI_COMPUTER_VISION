import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread("building1.jpg")
img2 = cv2.imread("building2.jpg")

orb = cv2.ORB_create()
kp1,des1 = orb.detectAndCompute(img1,None)
kp2,des2 = orb.detectAndCompute(img2,None)

brute_force = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = brute_force.match(des1,des2)


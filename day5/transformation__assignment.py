import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("cat.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# trasformation 

M =np.float32([[1,0,50],[0,1,50]])

transformation = cv2.warpAffine(img,M,(img.shape[1],img.shape[0]))

plt.imshow(transformation)
plt.show()

# rotation

M = cv2.getRotationMatrix2D((img.shape[1]//2,img.shape[0]//2),50,1)
rotation = cv2.warpAffine(img,M,(img.shape[1],img.shape[0]))

plt.imshow(rotation)
plt.show()

scal = cv2.resize(img,None,fx=0.1,fy=0.4)

plt.imshow(scal)
plt.show()
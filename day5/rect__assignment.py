import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("cat.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

rect = cv2.rectangle(img,(100,50),(350,350),(255,50,0),2)

plt.imshow(rect)
plt.show()
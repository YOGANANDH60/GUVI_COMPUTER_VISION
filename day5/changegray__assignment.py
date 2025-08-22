import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("cat.jpg")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


plt.imshow(gray)
plt.show()
import cv2
import matplotlib.pyplot as plt


img = cv2.imread("summa.jpg")
h,w = img.shape[:2]

cv2.circle(img,(150,150),50,(255, 0, 0),5)
# cropped = img[50:250,100:150]


img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
rm = cv2.getRotationMatrix2D((w//2,h//2),90,1)

rotated_img = cv2.warpAffine(img, rm, (w, h))

plt.imshow(rotated_img)
plt.axis('off')
plt.show()

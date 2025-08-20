import cv2
import matplotlib.pyplot as plt


img = cv2.imread("summa.jpg")
print(img.shape)
# rectangle

# cv2.rectangle(img,(30,30),(150,150),(255,0,0),2)
# cropped
# cropped = img[50:250,100:150]



h,w = img.shape[:2]
m = cv2.getRotationMatrix2D((w//2,h//2),90,1)
rotated = cv2.warpAffine(img,m,(h,w))
plt.imshow(cv2.cvtColor(rotated,cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()
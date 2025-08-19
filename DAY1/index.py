import cv2
import matplotlib.pyplot as plt


img = cv2.imread("summa.jpg")
print(img.shape)

cv2.rectangle(img,(30,30),(150,150),(255,0,0),2)
cropped = img[50:250,100:150]

img = cv2.cvtColor(cropped, cv2.COLOR_BGR2RGB)


plt.imshow(img)
plt.axis('off')
plt.show()

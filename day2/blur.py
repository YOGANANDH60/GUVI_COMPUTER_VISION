import cv2
import matplotlib.pyplot as plt

img = cv2.imread("summa.jpg")

# blur = cv2.blur(img,(5,5))
# plt.imshow(cv2.cvtColor(blur,cv2.COLOR_BGR2RGB))
# plt.axis("off")
# plt.show()

# median = cv2.medianBlur(img,5)
# plt.imshow(cv2.cvtColor(median,cv2.COLOR_BGR2RGB))
# plt.axis("off")
# plt.show()



gaussian = cv2.GaussianBlur(img,(5,5),0)
plt.imshow(cv2.cvtColor(gaussian,cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()
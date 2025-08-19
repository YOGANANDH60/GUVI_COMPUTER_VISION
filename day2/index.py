import cv2
import matplotlib.pyplot as plt


img = cv2.imread("summa.jpg")
h,w = img.shape[:2]

# cv2.circle(img,(150,150),50,(255, 0, 0),5)
# # cropped = img[50:250,100:150]

# # rm = cv2.getRotationMatrix2D((w//2,h//2),90,1)
# # rotated_img = cv2.warpAffine(img, rm, (w, h))
# plt.imshow(cv2.cvtColor(rotated_img, cv2.COLOR_BGR2RGB))
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# edges = cv2.Canny(gray,100,300)
# plt.imshow(cv2.cvtColor(edges, cv2.COLOR_BGR2RGB))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
threshold , thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
plt.imshow(cv2.cvtColor(thresh, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()

import cv2
import matplotlib.pyplot as plt

img = cv2.imread("cat.jpg", cv2.IMREAD_GRAYSCALE)


thresh_val, binary_img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

print("Optimal Threshold Value (Otsu):", thresh_val)



plt.subplot(1,2,1)
plt.title("Grayscale Image")
plt.imshow(img, cmap="gray")
plt.axis("off")

plt.subplot(1,2,2)
plt.title("Binary Image (Otsu)")
plt.imshow(binary_img, cmap="gray")
plt.axis("off")

plt.show()

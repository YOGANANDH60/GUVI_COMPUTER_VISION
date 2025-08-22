import cv2
import matplotlib.pyplot as plt

# Read image
img = cv2.imread("cat.jpg")  
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Average Blur
avg_blur = cv2.blur(img, (10, 9)) 

# Gaussian Blur
gaussian_blur = cv2.GaussianBlur(img, (15, 5), 0)

# Median Blur
median_blur = cv2.medianBlur(img, 7)

# result
titles = ['Original Image', 'Average Blur', 'Gaussian Blur', 'Median Blur']
images = [img, avg_blur, gaussian_blur, median_blur]

plt.figure(figsize=(10, 8))
for i in range(4):
    plt.subplot(2, 2, i + 1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.axis("off")

plt.show()

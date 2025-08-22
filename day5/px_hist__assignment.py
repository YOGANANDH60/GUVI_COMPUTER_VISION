import cv2
import matplotlib.pyplot as plt


img = cv2.imread("summa.jpg")
h, w = img.shape[:2]

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY)

# Histogram of grayscale intensities
hist = cv2.calcHist([gray], [0], None, [256], [0,256])

# Plot histogram
plt.plot(hist, color='black')
plt.title("Grayscale Histogram")
plt.xlabel("Pixel Intensity (0–255)")
plt.ylabel("Frequency")
plt.show()

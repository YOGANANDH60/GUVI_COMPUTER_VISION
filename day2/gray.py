import cv2


image = cv2.imread("summa.jpg")  

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


cv2.imwrite("grayscale.jpg", gray_image)

# Display the original and grayscale
cv2.imshow("Original Image", image)
cv2.imshow("Grayscale Image", gray_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

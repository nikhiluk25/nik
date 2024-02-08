import cv2
import numpy as np

# Load an image
image = cv2.imread("C:/Users/nikhi/Downloads/WhatsApp Image 2024-02-07 at 10.26.02 PM.jpeg", cv2.IMREAD_GRAYSCALE)

# Define the kernel for erosion and dilation
kernel = np.ones((5, 5), np.uint8)  # Kernel size can be adjusted as needed

# Perform erosion
eroded_image = cv2.erode(image, kernel, iterations=1)

# Perform dilation
dilated_image = cv2.dilate(image, kernel, iterations=1)

# Display the original, eroded, and dilated images
cv2.imshow('Original Image', image)
cv2.imshow('Eroded Image', eroded_image)
cv2.imshow('Dilated Image', dilated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
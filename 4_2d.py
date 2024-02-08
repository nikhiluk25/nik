import cv2

# Load a sample 2D image
image_2d = cv2.imread("C:/Users/nikhi/Downloads/pic.jpg")

# Specify the rotation angle in degrees
angle = 45

# Get the dimensions of the image
height, width = image_2d.shape[:2]

# Calculate the rotation matrix
rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), angle, 1)

# Apply the rotation to the image
rotated_image_2d = cv2.warpAffine(image_2d, rotation_matrix, (width, height))

# Display the original and rotated images
cv2.imshow('Original 2D Image', image_2d)
cv2.imshow('Rotated 2D Image', rotated_image_2d)
cv2.waitKey(0)
cv2.destroyAllWindows()
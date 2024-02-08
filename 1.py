import cv2
import numpy as np

# Create a blank image
               # image size                   #width*height
image = np.zeros((512, 512, 3), dtype="uint8")  # 512x512 pixels, 3 channels (BGR)

cv2.rectangle(image, (50, 50), (200, 150), (255, 0, 0), 1)  # (image, top-left corner, bottom-right corner, blue filled, thickness)

cv2.circle(image, (300, 100), 50, (0, 255, 0), -1)  # (image, center, radius, green filled, thickness)

cv2.line(image, (100, 300), (300, 300), (0, 0, 255), 2)  # (image, start point, end point, red, thickness)

# Display the image
cv2.imshow("Objects Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
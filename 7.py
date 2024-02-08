import cv2
import numpy as np

# Global variables
triangle_color = (0, 255, 0)  # Initial color (green)

# Function to draw a triangle with centroid
def draw_triangle(image, vertices):
    # Draw the triangle
    cv2.polylines(image, [vertices], isClosed=True, color=triangle_color, thickness=2)
    
    # Calculate centroid of the triangle
    centroid = np.mean(vertices, axis=0, dtype=np.int32)
    
    # Draw the centroid as a small circle
    cv2.circle(image, tuple(centroid), 3, (255, 0, 0), -1)
    
    return image

# Mouse callback function
def mouse_callback(event, x, y, flags, param):
    global triangle_color
    
    if event == cv2.EVENT_LBUTTONDOWN:
        # Change the color of the triangle when left mouse button is clicked
        triangle_color = (0, 0, 255)  # Change color to red
    elif event == cv2.EVENT_RBUTTONDOWN:
        # Change the color of the triangle when right mouse button is clicked
        triangle_color = (0, 255, 0)  # Change color to green

# Create a black canvas
canvas = np.zeros((512, 512, 3), dtype=np.uint8)

# Define the vertices of the triangle
triangle_vertices = np.array([[250, 100], [150, 300], [350, 300]], dtype=np.int32)

# Display instructions
print("Left click: Change triangle color to red")
print("Right click: Change triangle color to green")
print("Press any key to exit")

# Main loop
while True:
    # Draw the triangle with centroid
    canvas_with_triangle = draw_triangle(canvas.copy(), triangle_vertices)
    
    # Display the image
    cv2.imshow('Triangle with Centroid', canvas_with_triangle)
    
    # Set mouse callback
    cv2.setMouseCallback('Triangle with Centroid', mouse_callback)
    
    # Check for key press
    key = cv2.waitKey(1) & 0xFF
    if key != 255:
        break

# Close all windows
cv2.destroyAllWindows()
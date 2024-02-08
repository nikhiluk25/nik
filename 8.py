import cv2
import numpy as np
import math

# Function to rotate a point around the origin
def rotate_point(point, angle_x, angle_y, angle_z):
    x, y, z = point
    # Rotation around X-axis
    x_new = x
    y_new = y * math.cos(angle_x) - z * math.sin(angle_x)
    z_new = y * math.sin(angle_x) + z * math.cos(angle_x)
    # Rotation around Y-axis
    x_new = x_new * math.cos(angle_y) + z_new * math.sin(angle_y)
    y_new = y_new
    z_new = -x_new * math.sin(angle_y) + z_new * math.cos(angle_y)
    # Rotation around Z-axis
    x_new = x_new * math.cos(angle_z) - y_new * math.sin(angle_z)
    y_new = x_new * math.sin(angle_z) + y_new * math.cos(angle_z)
    z_new = z_new
    return [x_new, y_new, z_new]

# Define the 8 vertices of the cube
vertices = np.array([
    [-1, -1, -1],
    [1, -1, -1],
    [1, 1, -1],
    [-1, 1, -1],
    [-1, -1, 1],
    [1, -1, 1],
    [1, 1, 1],
    [-1, 1, 1]
])

# Define the 12 edges of the cube
edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),
    (4, 5), (5, 6), (6, 7), (7, 4),
    (0, 4), (1, 5), (2, 6), (3, 7)
]

# Define the color combinations for the edges
colors = [
    (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0),
    (255, 0, 255), (0, 255, 255), (255, 255, 255), (128, 0, 0),
    (0, 128, 0), (0, 0, 128), (128, 128, 0), (128, 0, 128)
]

# Rotation angles
angle_x = 0
angle_y = 0
angle_z = 0

# Create a black canvas
canvas = np.zeros((512, 512, 3), dtype=np.uint8)

# Main loop
while True:
    # Clear canvas
    canvas.fill(0)

    # Rotate vertices
    rotated_vertices = [rotate_point(vertex, angle_x, angle_y, angle_z) for vertex in vertices]

    # Draw edges
    for i, (p1, p2) in enumerate(edges):
        # Get vertices of the edge
        vertex1 = rotated_vertices[p1]
        vertex2 = rotated_vertices[p2]
        # Convert 3D coordinates to 2D coordinates for display
        x1, y1 = int(200 * vertex1[0] + 256), int(200 * vertex1[1] + 256)
        x2, y2 = int(200 * vertex2[0] + 256), int(200 * vertex2[1] + 256)
        # Draw the edge
        cv2.line(canvas, (x1, y1), (x2, y2), colors[i], 2)

    # Display the image
    cv2.imshow('Cube with Rotation', canvas)

    # Check for key press
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):  # Press 'q' to exit
        break
    elif key == ord('x'):  # Press 'x' to rotate around X-axis
        angle_x += 0.1
    elif key == ord('y'):  # Press 'y' to rotate around Y-axis
        angle_y += 0.1
    elif key == ord('z'):  # Press 'z' to rotate around Z-axis
        angle_z += 0.1

# Close all windows
cv2.destroyAllWindows()
import cv2
import numpy as np

# Create a blank canvas
canvas = np.zeros((400, 600, 3), dtype=np.uint8)

# Define background color as light gray
background_color = (211, 211, 211)  # Light Gray

# Fill the canvas with the background color
canvas[:, :] = background_color

# Initialize bird position and velocity
bird_x, bird_y = 50, 50
velocity_x, velocity_y = 2, -1

# Initialize car position and velocity
car_x, car_y = 300, 300
car_velocity = 3

# Define bird shape
bird_shape = np.array([[0, -10], [20, -5], [40, -10], [50, 0], [40, 10], [20, 5], [0, 0]], np.int32)

# Define car shape
car_shape = np.array([[0, 0], [30, 0], [30, 15], [20, 20], [10, 15], [0, 10]], np.int32)

# Define the number of iterations
iterations = 200

# Loop for the specified number of iterations
for _ in range(iterations):
    # Update bird position
    bird_x += velocity_x
    bird_y += velocity_y

    # Update car position
    car_x += car_velocity

    # Clear the canvas to the background color
    canvas[:, :] = background_color

    # Draw sun as orange circle
    cv2.circle(canvas, (500, 100), 50, (255, 165, 0), -1)  # Orange color for sun

    # Draw apartment building
    cv2.rectangle(canvas, (150, 200), (250, 400), (192, 192, 192), -1)  # Light Gray color for building
    cv2.rectangle(canvas, (200, 150), (300, 200), (105, 105, 105), -1)  # Dark Gray color for another part of the building

    # Draw windows on the building
    for i in range(3):
        for j in range(4):
            window_x = 160 + i * 30
            window_y = 210 + j * 30
            cv2.rectangle(canvas, (window_x, window_y), (window_x + 20, window_y + 20), (255, 248, 220), -1)  # Beige color for window

    # Draw trees
    cv2.rectangle(canvas, (350, 200), (370, 400), (139, 69, 19), -1)  # Brown color for tree trunk
    cv2.rectangle(canvas, (360, 100), (380, 200), (34, 139, 34), -1)  # Forest green color for tree top

    # Draw flowers
    for i in range(3):
        flower_x = 450 + i * 30
        flower_y = 350
        cv2.circle(canvas, (flower_x, flower_y), 10, (255, 20, 147), -1)  # Deep Pink color for flowers

    # Draw clouds
    cv2.ellipse(canvas, (100, 100), (60, 30), 0, 0, 360, (255, 255, 255), -1)
    cv2.ellipse(canvas, (180, 120), (80, 20), 0, 0, 360, (255, 255, 255), -1)
    cv2.ellipse(canvas, (280, 80), (50, 25), 0, 0, 360, (255, 255, 255), -1)

    # Draw the bird (change color to dark red)
    bird_points = bird_shape + [bird_x, bird_y]
    cv2.fillPoly(canvas, [bird_points], (139, 0, 0))  # Dark Red color for bird

    # Draw the car (change color to light blue)
    car_points = car_shape + [car_x, car_y]
    cv2.fillPoly(canvas, [car_points], (173, 216, 230))  # Light Blue color for car

    # Show the canvas
    cv2.imshow('Scenery with Apartment ', canvas)

    # Exit if 'q' is pressed or if the last iteration is reached
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Create a 3D cube
vertices_cube = np.array([
    [0, 0, 0],
    [1, 0, 0],
    [1, 1, 0],
    [0, 1, 0],
    [0, 0, 1],
    [1, 0, 1],
    [1, 1, 1],
    [0, 1, 1]
])

# Original cube
faces_cube = [[vertices_cube[j] for j in [0, 1, 2, 3, 0]],
              [vertices_cube[j] for j in [4, 5, 6, 7, 4]],
              [vertices_cube[j] for j in [0, 3, 7, 4, 0]],
              [vertices_cube[j] for j in [1, 2, 6, 5, 1]],
              [vertices_cube[j] for j in [0, 1, 5, 4, 0]],
              [vertices_cube[j] for j in [2, 3, 7, 6, 2]]]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.add_collection3d(Poly3DCollection(faces_cube, facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))
ax.set_xlim([0, 1])
ax.set_ylim([0, 1])
ax.set_zlim([0, 1])

# Define the rotation angle in degrees
angle = 45

# Define rotation matrix for rotating around z-axis
rotation_matrix = np.array([[np.cos(np.radians(angle)), -np.sin(np.radians(angle)), 0],
                            [np.sin(np.radians(angle)), np.cos(np.radians(angle)), 0],
                            [0, 0, 1]])

# Rotate the vertices of the cube
vertices_cube_rotated = np.dot(vertices_cube, rotation_matrix.T)

# Rotated cube
faces_cube_rotated = [[vertices_cube_rotated[j] for j in [0, 1, 2, 3, 0]],
                      [vertices_cube_rotated[j] for j in [4, 5, 6, 7, 4]],
                      [vertices_cube_rotated[j] for j in [0, 3, 7, 4, 0]],
                      [vertices_cube_rotated[j] for j in [1, 2, 6, 5, 1]],
                      [vertices_cube_rotated[j] for j in [0, 1, 5, 4, 0]],
                      [vertices_cube_rotated[j] for j in [2, 3, 7, 6, 2]]]

ax.add_collection3d(Poly3DCollection(faces_cube_rotated, facecolors='magenta', linewidths=1, edgecolors='b', alpha=.25))

plt.show()
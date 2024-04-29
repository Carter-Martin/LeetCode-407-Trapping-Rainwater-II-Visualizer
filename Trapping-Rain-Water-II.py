from vpython import canvas, box, color, vector, scene, local_light, distant_light
import hashlib
import random


height_map = [[1, 4, 3, 1, 3, 2], [3, 2, 1, 3, 2, 4], [2, 3, 3, 2, 3, 1]]
height_map = height_map[::-1]

num_rows = len(height_map)
num_cols = len(height_map[0])

# Calculate the center position of the structure
center_x = (num_rows - 1) / 2
center_z = (num_cols - 1) / 2

scene = canvas(title="Trapping Rain Water II Visualization", width=1600, height=800, center=vector(center_x, 0, center_z), background=color.white)

# Define the dimensions of the cubes
cube_size = 1  # Length of each side of the cube

fixed_colors = {
    1: color.blue,
    2: color.green,
    3: color.yellow,
    4: color.orange,
    5: color.red
}

# Create the height map of cubes
for row in range(num_rows):
    for col in range(num_cols):
        # Get the height of the current cube
        height = height_map[row][col]

        # Calculate the color based on height
        if 1 <= height <= 5:
            cube_color = fixed_colors[height]
        else:
            # Calculate a deterministic color for heights outside 1-5 range
            height_str = str(height)
            hash_object = hashlib.sha256(height_str.encode())
            hash_hex = hash_object.hexdigest()
            seed = int(hash_hex, 16)
            random.seed(seed)
            hue = random.random()  # Random hue value
            saturation = 1.0  # Full saturation
            value = 1.0  # Full brightness
            cube_color = color.hsv_to_rgb(vector(hue, saturation, value))

        # Calculate the position of the cube
        x_pos = row
        y_pos = -height * 0.5
        z_pos = col  # Start from the base row/column position

        # Create the cube
        cube = box(
            pos=vector(x_pos, y_pos + height, z_pos),
            length=cube_size,
            height=height * cube_size,
            width=cube_size,
            color=cube_color
        )

# Camera movement function
def move_camera(event):
    key = event.key
    if key == 'w':
        scene.camera.pos += vector(0, 0, 0.5)
    elif key == 's':
        scene.camera.pos -= vector(0, 0, 0.5)
    elif key == 'a':
        scene.camera.pos -= vector(0.5, 0, 0)
    elif key == 'd':
        scene.camera.pos += vector(0.5, 0, 0)

# Bind the camera movement function to keyboard events
scene.bind('keydown', move_camera)

# Add a distant light source
distant_light(direction=vector(-1, -1, -1), color=color.white)

# Add a very low intensity local light for ambient illumination
local_light(pos=vector(0, 10, 0), color=color.gray(0.01))

# Keep the window open until closed manually
print("Press Enter to close.")
input()

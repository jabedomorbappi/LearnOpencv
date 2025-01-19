import numpy as np
import cv2
from req import four_point_transform  # Ensure this module is correctly imported

# Define the path to the image and the coordinates directly in the script
image_path = "first/oen.png"
coords = [(101, 185), (393, 151), (479, 323), (187, 441)]  # Hardcoded coordinates

# Load the image
image = cv2.imread(image_path)

if image is None:
    raise FileNotFoundError(f"Image not found at path: {image_path}")

# Convert the coordinates to a NumPy array
pts = np.array(coords, dtype="float32")

# Apply the four-point transform
warped = four_point_transform(image, pts)

# Show the original and warped images
cv2.imshow("Original", image)
cv2.imshow("Warped", warped)
cv2.waitKey(0)
cv2.destroyAllWindows()

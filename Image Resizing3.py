import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import os

# Define the path to the image file
image_path = '/Users/kdmac/Downloads/test2.jpg'

# Check if the file exists
if not os.path.exists(image_path):
    raise FileNotFoundError(f"File not found: {image_path}")

# Load the image
img = cv.imread(image_path)
assert img is not None, "file could not be read, check with os.path.exists()"

# Get image dimensions
rows, cols, ch = img.shape

# Define points for perspective transformation
pts1 = np.float32([[56, 65], [368, 52], [28, 387], [389, 390]])
pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])

# Calculate the perspective transformation matrix
M = cv.getPerspectiveTransform(pts1, pts2)

# Apply the perspective transformation
dst = cv.warpPerspective(img, M, (300, 300))

# Display the original and transformed images using Matplotlib
plt.subplot(121), plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB)), plt.title('Input')
plt.subplot(122), plt.imshow(cv.cvtColor(dst, cv.COLOR_BGR2RGB)), plt.title('Output')
plt.show()

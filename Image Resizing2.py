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

# Define points for affine transformation
pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])

# Calculate the affine transformation matrix
M = cv.getAffineTransform(pts1, pts2)

# Apply the affine transformation
dst = cv.warpAffine(img, M, (cols, rows))

# Display the original and transformed images using Matplotlib
plt.subplot(121), plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB)), plt.title('Input')
plt.subplot(122), plt.imshow(cv.cvtColor(dst, cv.COLOR_BGR2RGB)), plt.title('Output')
plt.show()

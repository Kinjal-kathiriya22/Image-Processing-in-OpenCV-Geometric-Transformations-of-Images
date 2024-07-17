import cv2 as cv
import numpy as np
import os

# Define the path to the image file
image_path = '/Users/kdmac/Downloads/test2.jpg'

# Check if the file exists
if not os.path.exists(image_path):
    raise FileNotFoundError(f"File not found: {image_path}")

# Load the image in grayscale mode
img = cv.imread(image_path, cv.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"

# Get the image dimensions
rows, cols = img.shape

# Define the rotation matrix
M = cv.getRotationMatrix2D(((cols-1)/2.0, (rows-1)/2.0), 90, 1)

# Apply the affine transformation (rotation)
dst = cv.warpAffine(img, M, (cols, rows))

# Display the original and rotated images
cv.imshow('Original Image', img)
cv.imshow('Rotated Image', dst)

# Wait for a key press and close all windows
cv.waitKey(0)
cv.destroyAllWindows()

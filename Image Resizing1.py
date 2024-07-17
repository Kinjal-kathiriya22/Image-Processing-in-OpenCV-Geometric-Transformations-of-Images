import numpy as np
import cv2 as cv
import os

# Define the path to the image file
image_path = '/Users/kdmac/Downloads/test2.jpg'

# Check if the file exists
if not os.path.exists(image_path):
    raise FileNotFoundError(f"File not found: {image_path}")

# Load the image
img = cv.imread(image_path)
assert img is not None, "file could not be read, check with os.path.exists()"

# Print the current working directory for debugging
print("Current working directory:", os.getcwd())

# Resize the image using two different methods

# Method 1: Resize with scaling factors
res1 = cv.resize(img, None, fx=2, fy=2, interpolation=cv.INTER_CUBIC)

# Method 2: Resize with new dimensions
height, width = img.shape[:2]
res2 = cv.resize(img, (2 * width, 2 * height), interpolation=cv.INTER_CUBIC)

# Display the original and resized images
cv.imshow('Original Image', img)
cv.imshow('Resized Image 1', res1)
cv.imshow('Resized Image 2', res2)

# Wait for a key press and close all windows
cv.waitKey(0)
cv.destroyAllWindows()

# -*- coding: utf-8 -*-
"""DIP-REMEDIAL-MALIK-20220040128.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ku8RKuTF0FW0bQq9yfDdTS8xIgCBRCfs
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread('/content/remedial.JPG')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Convert the image to HSV color space
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define the range of the color to detect (example: red)
lower_red = np.array([0, 120, 70])  # Lower bound of HSV range
upper_red = np.array([10, 255, 255])  # Upper bound of HSV range

# Create a mask for the red color
mask = cv2.inRange(hsv_image, lower_red, upper_red)

# Find contours (edges) of the detected objects
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Filter small contours based on a minimum area to remove noise
min_area = 100  # Minimum area to consider an object
filtered_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > min_area]

# Count the number of detected objects
num_objects = len(filtered_contours)

# Draw the contours on the original image for visualization
image_with_contours = image_rgb.copy()
cv2.drawContours(image_with_contours, filtered_contours, -1, (0, 255, 0), 2)  # Green contours

# Display the original image, mask, detection result, and contours
plt.figure(figsize=(15, 8))

# Original image
plt.figure(figsize=(32, 16))
plt.subplot(1, 4, 1)
plt.title("Original Image")
plt.imshow(image_rgb)
plt.axis('off')

# Mask
plt.figure(figsize=(32, 16))
plt.subplot(1, 4, 2)
plt.title("Mask")
plt.imshow(mask, cmap='gray')
plt.axis('off')

# Detection result
plt.figure(figsize=(32, 16))
result = cv2.bitwise_and(image_rgb, image_rgb, mask=mask)
plt.subplot(1, 4, 3)
plt.title("Detection Result")
plt.imshow(result)
plt.axis('off')

# Image with contours
plt.figure(figsize=(24, 12))
plt.subplot(1, 4, 4)
plt.title(f"Detected Objects: {num_objects}")
plt.imshow(image_with_contours)
plt.axis('off')

plt.tight_layout()
plt.show()

# Print the number of objects detected
print(f"Number of objects detected: {num_objects}")
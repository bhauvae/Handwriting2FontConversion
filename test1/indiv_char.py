import cv2
import numpy as np

# Load image
image = cv2.imread('char_page_1.png')

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Thresholding (adjust parameters as needed)
_, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

# Find contours
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Draw contours to extract grid lines (optional)
cv2.drawContours(image, contours, -1, (0, 255, 0), 3)

# Find grid lines using Hough Line Transform
lines = cv2.HoughLines(thresh, 1, np.pi / 180, 200)

# Draw lines (optional)
if lines is not None:
    for rho, theta in lines[:, 0]:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))
        cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)

# Extract cells
# Implement logic to extract cells from the grid lines detected

# Save individual cells as separate PNGs
# Implement logic to save individual cells as PNG files

# Display the image with grid lines (optional)
cv2.imshow('Grid Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import numpy as np

# Read the image and the trimap
img = cv2.imread('images/Abyssinian_4.jpg')
trimap = cv2.imread('annotations/trimaps/._Abyssinian_4.png')

# Convert to HSV color space
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
trimap_hsv = cv2.cvtColor(trimap, cv2.COLOR_BGR2HSV)

# Define lower and upper range of colors for foreground and background
lower_fg = np.array([0, 0, 200])
upper_fg = np.array([180, 255, 255])
lower_bg = np.array([0, 0, 0])
upper_bg = np.array([180, 255, 50])

# Create masks for foreground and background
mask_fg = cv2.inRange(trimap_hsv, lower_fg, upper_fg)
mask_bg = cv2.inRange(trimap_hsv, lower_bg, upper_bg)

# Combine masks
mask = cv2.bitwise_or(mask_fg, mask_bg)

# Apply mask to image
output = cv2.bitwise_and(img_hsv, img_hsv, mask=mask)

# Save output image
cv2.imwrite('output.png', output)

import os
import cv2
import numpy as np

# Get the list of files in the images folder
files = os.listdir("images/train/")

# Loop through each file
for file in files:
    # Check if the file is an image
    if file.endswith(".jpg"):
        # Load the image and the trimap as grayscale images
        image = cv2.imread("images/train/" + file)
        trimap = cv2.imread("annotations/trimaps/" + file[:-4] + ".png", cv2.IMREAD_GRAYSCALE)

        mask = np.zeros(trimap.shape, np.uint8)
        mask[trimap == 2] = cv2.GC_BGD # background
        mask[trimap == 1] = cv2.GC_FGD # foreground
        mask[trimap == 0] = cv2.GC_PR_FGD # probably foreground

        # Create a binary mask for the foreground and background regions
        fg_mask = np.where((mask == cv2.GC_FGD) | (mask == cv2.GC_PR_FGD), 255, 0).astype(np.uint8)
        bg_mask = np.where((mask == cv2.GC_BGD) | (mask == cv2.GC_PR_BGD), 255, 0).astype(np.uint8)

        # Apply bitwise operations to extract the foreground and background pixels from the image using the mask
        fg = cv2.bitwise_and(image, image, mask=fg_mask)
        bg = cv2.bitwise_and(image, image, mask=bg_mask)

        # write the results
        cv2.imwrite("images/filtered_train/" + file, fg)

# Get the list of files in the images folder
files = os.listdir("images/val/")

# Loop through each file
for file in files:
    # Check if the file is an image
    if file.endswith(".jpg"):
        # Load the image and the trimap as grayscale images
        image = cv2.imread("images/val/" + file)
        trimap = cv2.imread("annotations/trimaps/" + file[:-4] + ".png", cv2.IMREAD_GRAYSCALE)

        mask = np.zeros(trimap.shape, np.uint8)
        mask[trimap == 2] = cv2.GC_BGD # background
        mask[trimap == 1] = cv2.GC_FGD # foreground
        mask[trimap == 0] = cv2.GC_PR_FGD # probably foreground

        # Create a binary mask for the foreground and background regions
        fg_mask = np.where((mask == cv2.GC_FGD) | (mask == cv2.GC_PR_FGD), 255, 0).astype(np.uint8)
        bg_mask = np.where((mask == cv2.GC_BGD) | (mask == cv2.GC_PR_BGD), 255, 0).astype(np.uint8)

        # Apply bitwise operations to extract the foreground and background pixels from the image using the mask
        fg = cv2.bitwise_and(image, image, mask=fg_mask)
        bg = cv2.bitwise_and(image, image, mask=bg_mask)

        # write the results
        cv2.imwrite("images/filtered_val/" + file, fg)

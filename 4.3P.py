import os
import random
import shutil

# Define the image classes and the split ratios
classes = ["shiba_inu", "american_bulldog", "basset_hound", "chihuahua"]
train_ratio = 0.4
val_ratio = 0.3
test_ratio = 0.3

# Set the directory where the images are stored
os.chdir("C:/Users/nsrih/Downloads/oxford-iiit-pet/images")

# Create the output directories for each split
os.makedirs("train", exist_ok=True)
os.makedirs("val", exist_ok=True)
os.makedirs("test", exist_ok=True)

# Loop over each class
for cls in classes:
    # Get the list of image files for that class
    files = [file for file in os.listdir() if file.startswith(cls)]
    # Shuffle the files randomly
    random.shuffle(files)
    # Calculate the number of files for each split
    n_train = int(len(files) * train_ratio)
    n_val = int(len(files) * val_ratio)
    n_test = len(files) - n_train - n_val
    # Copy the files to the corresponding output directories
    for i, file in enumerate(files):
        src = file
        if i < n_train:
            dst = os.path.join("train", file)
        elif i < n_train + n_val:
            dst = os.path.join("val", file)
        else:
            dst = os.path.join("test", file)
        shutil.copy(src, dst)

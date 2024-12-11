from PIL import Image
import os

# Folder containing images
folder_path = './images'

# Desired size
size = (250, 250)

# Loop through all files in the folder
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    
    # Open image and resize it
    with Image.open(file_path) as img:
        img = img.resize(size)
        # Save resized image, overwriting the original
        img.save(file_path)

print("All images have been resized to 250x250.")

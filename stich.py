from PIL import Image
import os

# Folder containing images
folder_path = './images'

# Loop through all files in the folder
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    
    # Check if the file is an image
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        with Image.open(file_path) as img:
            # Get the size of the original image
            width, height = img.size
            
            # Create a new blank image with size 2x width and 2x height
            new_img = Image.new('RGB', (width * 2, height * 2))
            
            # Paste the original image into the 2x2 grid
            new_img.paste(img, (0, 0))
            new_img.paste(img, (width, 0))
            new_img.paste(img, (0, height))
            new_img.paste(img, (width, height))
            
            # Save the new stitched image, replacing the original
            new_img.save(file_path)

print("Images have been stitched and saved in place of the original images.")

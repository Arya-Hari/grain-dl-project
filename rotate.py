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
            # Rotate image by 90, 180, and 270 degrees and save each one
            for angle in [90, 180, 270]:
                rotated_img = img.rotate(angle, expand=True)
                
                # Create new filename for the rotated image
                new_filename = f"{os.path.splitext(filename)[0]}_{angle}deg{os.path.splitext(filename)[1]}"
                rotated_img.save(os.path.join(folder_path, new_filename))

print("Images have been rotated and saved separately.")

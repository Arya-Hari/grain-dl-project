import cv2
import numpy as np
from PIL import Image
import os

# YOLOv5 label format: <class> <x_center> <y_center> <width> <height>
def save_yolo_label(filename, label, x_center, y_center, width, height, img_width, img_height):
    with open(filename, 'a') as f:
        # Normalize the coordinates by dividing by image dimensions
        x_center_norm = x_center / img_width
        y_center_norm = y_center / img_height
        width_norm = width / img_width
        height_norm = height / img_height
        
        # Write the label in YOLO format
        f.write(f"{label} {x_center_norm} {y_center_norm} {width_norm} {height_norm}\n")

# Load the image using PIL
image = Image.open('./images/rice (16).png')

# Convert the image to OpenCV format (BGR)
opencv_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

# Convert the image to HSV color space
hsv_image = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2HSV)

# Refined color ranges for white and yellow rice in HSV
# White rice: high value (brightness), low saturation
lower_white = np.array([0, 0, 190])  # Loosened value threshold
upper_white = np.array([180, 100, 255])

# Yellow rice: specific hue, moderate saturation and value
lower_yellow = np.array([20, 70, 70])
upper_yellow = np.array([30, 255, 255])

# Create masks for detecting white and yellow rice grains
mask_white = cv2.inRange(hsv_image, lower_white, upper_white)
mask_yellow = cv2.inRange(hsv_image, lower_yellow, upper_yellow)

# Visualize the masks for debugging purposes
#cv2.imwrite("white_mask.png", mask_white)  # To see white rice mask
#cv2.imwrite("yellow_mask.png", mask_yellow)  # To see yellow rice mask

# Combine the masks to detect all rice grains
combined_mask = cv2.bitwise_or(mask_white, mask_yellow)

# Find contours using the combined mask
contours, _ = cv2.findContours(combined_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Color codes for drawing bounding boxes
good_rice_color = (36, 255, 240)  # #f0ff24 in BGR
coloured_rice_color = (6, 6, 239)  # #ef0606 in BGR

# Directory to save the YOLO labels
labels_dir = './yolo_labels/'
os.makedirs(labels_dir, exist_ok=True)

# Image dimensions
img_height, img_width = opencv_image.shape[:2]

padding = 5  # Pixels to expand the bounding box

# Iterate over contours to draw bounding boxes and save YOLOv5 labels
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)

    x = max(0, x - padding)
    y = max(0, y - padding)
    w = min(img_width - x, w + 2 * padding)
    h = min(img_height - y, h + 2 * padding)
    
    # Calculate the center coordinates of the bounding box
    x_center = x + w / 2
    y_center = y + h / 2

    # Extract the region of interest (ROI)
    roi = hsv_image[y:y+h, x:x+w]

    # Calculate the mean color in the HSV space
    mean_hue, mean_saturation, mean_value = cv2.mean(roi)[:3]

    # Debug the mean values for more insight
    print(f"Mean Hue: {mean_hue}, Mean Saturation: {mean_saturation}, Mean Value: {mean_value}")

    # Label based on refined HSV values
    if 5 <= mean_hue <= 12 and mean_saturation > 27:  # Coloured rice (yellow, with moderate saturation)
        label = 1  # Class for coloured-rice
        bbox_color = coloured_rice_color
        label_text = "coloured-rice"
    elif mean_value > 25 and mean_saturation < 20:  # Good rice (white, low saturation, high value)
        label = 0  # Class for good-rice
        bbox_color = good_rice_color
        label_text = "good-rice"
    else:
        continue  # Skip if it's not clearly identified

    # Save the YOLOv5 label to a text file
    label_filename = os.path.join(labels_dir, 'rice (16).txt')
    save_yolo_label(label_filename, label, x_center, y_center, w, h, img_width, img_height)

    # Draw the bounding box around the rice grain
    cv2.rectangle(opencv_image, (x, y), (x+w, y+h), bbox_color, 1)
    
    # Put the label above the bounding box
    #cv2.putText(opencv_image, label_text, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.4, bbox_color, 1)

# Convert the image back to RGB format for displaying
result_image = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2RGB)
result_pil_image = Image.fromarray(result_image)

# Save the resultant image with bounding boxes and labels
result_image_path_updated = './rice_with_bboxes_labeled.png'
result_pil_image.save(result_image_path_updated)

# Output the saved image path
result_image_path_updated

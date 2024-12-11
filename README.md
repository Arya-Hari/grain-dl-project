# Deep Learning Approach for Grain Quality Analysis

## Objective
The project aims to develop a rice grain quality detection system using deep learning. The goal is to classify rice grains based on quality parameters such as color, size, shape, and the presence of impurities. This system leverages YOLO (You Only Look Once) to analyze images of rice grains, identify different types of rice grains, and determine the number of each type to assess the quality of the rice sample. The approach focuses primarily on distinguishing colored rice from good-quality rice, automating the process to replace manual inspection.

## Dataset Preparation
1. **Capture Images**: 
   - Images were captured using a phone camera from a fixed height, with approximately 20 grains per image, maintaining a good ratio of white and colored rice (dyed yellow for research purposes). 
   - Four initial images were taken, which were later augmented to increase the dataset size.

2. **Resize the Images**: 
   - All images were resized to a 250x250 dimension using an automated Python script to standardize quality.

3. **Remove Background**: 
   - To improve model training, the backgrounds of all images were replaced with a solid black color using an AI tool, enhancing the contrast between the rice grains and the background.

4. **Rotate the Images**: 
   - As part of data augmentation, each image was rotated by 90, 180, and 270 degrees, increasing the dataset size from 4 images to 16.

5. **Stitch the Images**: 
   - Images were combined into a 2x2 grid, resulting in 16 photos with around 100 rice grains each.

6. **Annotate the Images**: 
   - Using OpenCV, a Python script detected rice grains and drew bounding boxes around them, labeling each as either "good-rice" or "colored-rice". Manual annotation was performed where automatic detection failed.

## Model Training
- The YOLOv5 model was trained on the augmented dataset using Roboflow. Roboflow Train was also employed to train an internal model with built-in augmentation techniques.
- Despite the small dataset, the recall and mAP (mean Average Precision) values were above 85%, indicating a reasonably good performance.

## Results
- The model achieved satisfactory results, successfully classifying rice grains into good and colored categories with proper labeling.
- Inference on images outside the training set demonstrated accurate classification.

## Tools and Technologies
- **Deep Learning Framework**: YOLOv5
- **Annotation Tools**: OpenCV, Roboflow
- **Languages**: Python
- **Image Processing**: AI-based background removal

## Future Work
- Increase the dataset size for better accuracy.
- Include additional quality parameters such as shape and size.
- Implement a real-time detection system for larger batches of grains.

## References
- [YOLOv5 Documentation](https://github.com/ultralytics/yolov5)
- [Roboflow](https://roboflow.com)
- [OpenCV Documentation](https://docs.opencv.org)
- [remove.bg](https://www.remove.bg/)

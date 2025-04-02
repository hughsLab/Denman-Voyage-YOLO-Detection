import cv2
import os

# Define the input directory and output video file
input_dir = r"C:\Users\hugh_mat\Desktop\voyage pics\YOLO output"
output_video = r"C:\Users\hugh_mat\Desktop\voyage pics\output_video.mp4"

# List all .jpg files in the input directory
images = [img for img in os.listdir(input_dir) if img.endswith('.jpg')]
images.sort()  # Sort images to maintain order

# Check if there are images to process
if not images:
    print("No images found in the directory.")
else:
    # Get the width and height of the first image to set video size
    first_image = cv2.imread(os.path.join(input_dir, images[0]))
    height, width, layers = first_image.shape

    # Create a video writer object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for .mp4
    video_writer = cv2.VideoWriter(output_video, fourcc, 6, (width, height))

    # Loop through the images and write them to the video
    for image in images:
        img_path = os.path.join(input_dir, image)
        frame = cv2.imread(img_path)
        video_writer.write(frame)  # Write the frame to the video

    # Release the video writer
    video_writer.release()
    print(f"Video created successfully: {output_video}")

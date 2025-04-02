from ultralytics import YOLO
import os

# Load a pretrained YOLO11n model
model = YOLO("yolo11n.pt")

# Define the source directory and output directory
source_dir = r"C:\Users\hugh_mat\Desktop\voyage pics"
output_dir = r"C:\Users\hugh_mat\Desktop\voyage pics\YOLO output"

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Loop through all image files in the source directory
for filename in os.listdir(source_dir):
    if filename.endswith(('.jpg', '.jpeg', '.png')):  # Check for image file extensions
        source = os.path.join(source_dir, filename)  # Full path to the image file
        
        # Run inference on the source
        results = model(source)  # list of Results objects
        
        # Save the output image in the output directory
        output_path = os.path.join(output_dir, f"output_{filename}")  # Modify filename for output
        results[0].save(output_path)  # Save the first result
import os
import time
import requests
from PIL import Image
import imageio.v2 as imageio  # Handle deprecation warning
import imageio_ffmpeg as ffmpeg  # Ensure ffmpeg is available

# Set the base URL of the webcam
base_url = "http://dirt.asrv.local/webcam/aft?timestamp=1741313141166"

# Set the directory where the images will be saved
save_dir = r"C:\Users\hugh_mat\Desktop\voyage pics"

# Ensure the save directory exists
os.makedirs(save_dir, exist_ok=True)

# Function to capture and save image
def capture_image(image_num):
    timestamp = int(time.time() * 1000)
    url = f"{base_url}?timestamp={timestamp}"
    response = requests.get(url)
    if response.status_code == 200 and 'image' in response.headers['Content-Type']:
        image_path = os.path.join(save_dir, f"image_{image_num:03d}.jpg")
        with open(image_path, "wb") as file:
            file.write(response.content)
        print(f"Saved image {image_num:03d}")
    else:
        print(f"Failed to capture image {image_num:03d}")

# Function to create a film from the images
def create_film(image_count):
    images = []
    for i in range(1, image_count + 1):
        image_path = os.path.join(save_dir, f"image_{i:03d}.jpg")
        if os.path.exists(image_path):
            images.append(imageio.imread(image_path))
    film_path = os.path.join(save_dir, "film.mp4")
    if images:
        try:
            imageio.mimwrite(film_path, images, fps=10)
            print(f"Created film with {image_count} images")
        except Exception as e:
            print(f"Failed to create film: {e}")
    else:
        print("No images to create a film")

# Main loop to capture images every 20 seconds and create film after 20 images
image_count = 0
while True:
    image_count += 1
    capture_image(image_count)
    if image_count % 100 == 0:
        create_film(100)
        image_count = 0  # Reset image count after creating the film
    time.sleep(5)

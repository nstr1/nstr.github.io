from PIL import Image
import os

image_folder = 'images/'

size = 512  # You can adjust this

for filename in os.listdir(image_folder):
    if filename.endswith(('jpg', 'jpeg', 'png')):
        image_path = os.path.join(image_folder, filename)
        
        with Image.open(image_path) as img:
            # Get the shortest dimension and crop the image to square
            min_dim = min(img.size)
            left = (img.width - min_dim) // 2
            top = (img.height - min_dim) // 2
            right = (img.width + min_dim) // 2
            bottom = (img.height + min_dim) // 2

            img_cropped = img.crop((left, top, right, bottom))
            img_resized = img_cropped.resize((size, size))  # Resize to fixed size

            img_resized.save(image_path)



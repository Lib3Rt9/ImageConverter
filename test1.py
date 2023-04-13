import os
from PIL import Image
import pathlib

path = pathlib.Path(__file__).parent.resolve()
os.chdir(path)

# Set the directory containing the HEIC images
heic_dir = path

# Loop through all files in the directory
for filename in os.listdir(heic_dir):
    # Check if the file is a HEIC image
    if filename.endswith('.HEIC'):
        # Open the HEIC image
        heic_image = Image.open(os.path.join(heic_dir, filename))
        # Convert the HEIC image to JPG
        jpg_image = heic_image.convert('RGB')
        # Save the JPG image with the same name as the HEIC image
        jpg_image.save(os.path.join(heic_dir, filename.replace('.heic', '.jpg')))
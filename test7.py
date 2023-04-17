import os
from PIL import Image
import pathlib
from pillow_heif import register_heif_opener
import pillow_heif

path = pathlib.Path(__file__).parent.resolve()
os.chdir(path)
img_ext = [".HEIC", ".heic"]

# Set the directory containing the HEIC images
heic_dir = path

# Loop through all files in the directory
for filename in os.listdir(heic_dir):
    # Check if the file is a HEIC image
    if filename.endswith(tuple(img_ext)):
        # Open the HEIC image using pillow_heif
        heif_image = pillow_heif.open_heif(os.path.join(heic_dir, filename))
        # Save the image as a JPG with a high quality setting
        heif_image.save(os.path.join(heic_dir, filename.replace('.HEIC', '.JPG')), quality=100)
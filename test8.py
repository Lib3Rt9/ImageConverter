import os
from PIL import Image
import pillow_heif
import pathlib

# Set the directory containing the HEIC images
# heic_dir = 'D:/test'
heic_dir = pathlib.Path(__file__).parent.resolve()
img_exts = (".HEIC", ".heic")

# Loop through all files in the directory
for filename in os.listdir(heic_dir):

    # Check if the file is a HEIC image
    if filename.endswith(img_exts):

        # Open the HEIC image using pillow_heif
        # heif_file = os.path.join(heic_dir, filename)
        # heif_file = os.path.normpath(heif_file)
        heif_image = pillow_heif.HeifFile(os.path.join(heic_dir, filename))
        # heif_image = pillow_heif.HeifFile(heif_file)
        
        # Save the image as a JPG with a high quality setting
        for img_ext in img_exts:
            heif_image.save(os.path.join(heic_dir, filename.replace(img_ext, '.JPG')), quality=100)

        # heif_image.save(os.path.join(heic_dir, filename.replace(img_exts[0], '.JPG').replace(img_exts[1], '.JPG')), quality=100)
        # heif_image.save(jpg_file, quality=100)

print(0)
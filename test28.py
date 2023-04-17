import os
from PIL import Image
import pillow_heif
import pathlib

# Set the directory containing the images
directory = pathlib.Path(__file__).parent.resolve()
img_exts = (".HEIC", ".heic", ".JPG", ".jpg", ".PNG", ".png", ".WEBP", ".webp")

# Set the source and target image formats
source_format = '.JPG'
target_format = '.HEIC'

def convert_to_heic(img_path):
    img = Image.open(img_path)
    img.show()
    heif_img = pillow_heif.from_pil_image(img)
    heif_img.save(img_path.replace(os.path.splitext(img_path)[1], target_format))

def convert_to_other(img_path):
    img = Image.open(img_path)
    img.show()
    img.save(img_path.replace(os.path.splitext(img_path)[1], target_format))

# Loop through all files in the directory
for filename in os.listdir(directory):

    # Check if the file is an image of the specified source format
    if filename.endswith(source_format):

        # Open the image using pillow_heif or PIL
        # img_path = os.path.join(directory, filename)
        img_path = os.path.join(filename)
        if source_format in (".HEIC", ".heic"):
            heif_image = pillow_heif.HeifFile(img_path)
            # Save the image in the target format
            heif_image.save(os.path.join(directory, filename.replace(os.path.splitext(filename)[1], target_format)))
        else:
            if target_format in (".HEIC", ".heic"):
                convert_to_heic(img_path)
            else:
                convert_to_other(img_path)

print(0)
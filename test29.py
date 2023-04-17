import os
from PIL import Image
import pillow_heif
from pillow_heif import register_heif_opener
import pathlib
import cv2
import numpy as np

# Set the directory containing the images
directory = pathlib.Path(__file__).parent.resolve()
img_exts = (".HEIC", ".heic", ".HEIF", ".heif", ".JPG", ".jpg", ".PNG", ".png", ".WEBP", ".webp")

# Set the source and target image formats
source_format = (".HEIC", ".heic", ".HEIF", ".heif")
target_format = (".jpg")

# pillow_heif.register_heif_opener()
register_heif_opener()

# Set whether to remove the original image files after conversion
remove_originals = True

def convert_to_heic(img_path):
    img = Image.open(img_path)
    img.show()
    heif_img = pillow_heif.from_pil_image(img)
    heif_img.save(img_path.replace(os.path.splitext(img_path)[1], target_format))

def convert_to_other(img_path):
    
    # try:
    #     img = Image.open(img_path)
    # except:
    #     # read image using cv2 as numpy array
    #     img = cv2.imread(img_path)
    #     # convert the color (necessary)
    #     img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    #     # read as PIL image in RGB
    #     img = Image.fromarray(img).convert("RGBA")
    # # except:
    # #     print("Could not convert this image")
    
    img = Image.open(img_path)
    img.show()
    img.save(img_path.replace(os.path.splitext(img_path)[1], target_format))

# Loop through all files in the directory
for filename in os.listdir(directory):

    # Check if the file is an image of the specified source format
    if filename.endswith(img_exts):

        # Open the image using pillow_heif or PIL
        img_path = os.path.join(directory, filename)
        # if source_format in (".HEIC", ".heic"):
        if filename.endswith(source_format):

            # heif_image = pillow_heif.HeifFile(img_path) # this code line is correct but use another way to open heif file as below
            # # Save the image in the target format
            # heif_image.save(os.path.join(directory, filename.replace(os.path.splitext(filename)[1], target_format))) # this code line is wrong since it saved in target_format but the images still is heif image, which might cause image to corrupted

            # open file as an object of Pillow
            img = Image.open(filename)
            # there is some quality loss when converting the original HEIC file to other format (PNG, JPG, WEBP) in this function
            img.save(os.path.join(directory, filename.replace(os.path.splitext(filename)[1], target_format)))

        else:
            if target_format in (".HEIC", ".heic", ".HEIF", ".heic"):
                convert_to_heic(img_path)
            else:
                convert_to_other(img_path)

        # Remove the original image file if specified
        if remove_originals:
            os.remove(img_path)
            print(100)

print(0)
import os
from PIL import Image
import pillow_heif
import pathlib

# Set the directory containing the images
heic_dir = pathlib.Path(__file__).parent.resolve()
img_exts = (".HEIC", ".heic", ".JPG", ".jpg", ".PNG", ".png", ".WEBP", ".webp")
# a= Image.open('D:\\Python\\Image_Converter\\IMG_1010.JPG')
def convert_to_heic(img_path):
    img = Image.open(img_path)
    heif_img = pillow_heif.from_pil_image(img)
    heif_img.save(img_path.replace(os.path.splitext(img_path)[1], '.HEIC'))

def convert_to_other(img_path, ext):
    img = Image.open(img_path)
    img.save(img_path.replace(os.path.splitext(img_path)[1], ext))

# Loop through all files in the directory
for filename in os.listdir(heic_dir):

    # Check if the file is an image
    if filename.endswith(img_exts):

        # Open the image using pillow_heif or PIL
        img_path = os.path.join(heic_dir, filename)
        if filename.endswith((".HEIC", ".heic")):
            heif_image = pillow_heif.HeifFile(img_path)
            # Save the image as a JPG with a high quality setting
            heif_image.save(os.path.join(heic_dir, filename.replace(os.path.splitext(filename)[1], '.JPG')), quality=100)
            # Save the image as a PNG
            heif_image.save(os.path.join(heic_dir, filename.replace(os.path.splitext(filename)[1], '.PNG')))
            # Save the image as a WEBP
            heif_image.save(os.path.join(heic_dir, filename.replace(os.path.splitext(filename)[1], '.WEBP')))
        else:
            convert_to_heic(img_path)
            convert_to_other(img_path, '.JPG')
            convert_to_other(img_path, '.PNG')
            convert_to_other(img_path, '.WEBP')

print(0)
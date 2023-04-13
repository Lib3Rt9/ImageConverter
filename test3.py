import os
from PIL import Image
import pathlib

path = pathlib.Path(__file__).parent.resolve()
os.chdir(path)

heic_dir = path
jpg_dir = path

for filename in os.listdir(heic_dir):
    if filename.endswith(".HEIC"):
        heic_image = Image.open(os.path.join(heic_dir, filename))
        rgb_heic_image = heic_image.convert("RGB")
        print(heic_image)
        jpg_image_path = os.path.join(jpg_dir, filename.replace(".heic", ".jpg"))

        rgb_heic_image.save(jpg_image_path, quality=95)
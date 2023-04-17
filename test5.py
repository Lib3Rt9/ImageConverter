import os
from PIL import Image
import pathlib
from pillow_heif import register_heif_opener
import pillow_heif

# path = input("path: ")
path = pathlib.Path(__file__).parent.resolve()
os.chdir(path)

# heif_dir = "D:\test\IMG_1010.HEIC"
jpg_dir = path

heif_image = pillow_heif.open_heif("IMG_1027.HEIC")
heif_image.save("image.jpg", quality=100)
img_ext = [".HEIC", ".heic"]
# file_count = sum(filename.endswith(tuple(img_ext)) for filename in os.listdir(heif_dir))

# print(file_count)

# for i in range(file_count):
# for filename in os.listdir(heif_dir):
#     if filename.endswith(tuple(img_ext)):
#         heif_image = pillow_heif.open_heif(os.path.join(heif_dir, filename))
#         heif_image.save("image" + str(i) +".jpg", quality=100)

        # rgb_heif_image = heif_image.convert("RGB")
        # print(heif_image)
        # jpg_image_path = os.path.join(jpg_dir, filename.replace(".heic", ".jpg"))

        # rgb_heif_image.save(jpg_image_path, quality=95)
print(1)

# heif_image = pillow_heif.open_heif("Ảnh 2023-03-26 02.59.17 CH.heic")

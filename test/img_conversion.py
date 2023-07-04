from PIL import Image
from pillow_heif import register_heif_opener
import pillow_heif

# img = Image.open("089q6tdzh20qg8s4zcr11c55mjna.jpg")
# img.show()

# register_heif_opener()
# img = Image.open("IMG_1027.HEIC")
heif_image = pillow_heif.open_heif("Ảnh 2023-03-26 02.59.17 CH.heic")

# convert to RGB format first
# img_rgb = img.convert("RGB")

# img_rgb.save("image.jpg", quality=100)

# # to PNG
# img_convert_2_png = img_rgb.save("a.png", "png")

# # to JPG
# img_convert_2_jpg = img_rgb.save("b.jpg", "jpeg")

# # to WEBP
# img_convert_2_webp = img_rgb.save("c.webp", "webp")

image = Image.frombytes(
    heif_image.mode,
    heif_image.size,
    heif_image.data,
    "raw",
    heif_image.mode,
    heif_image.stride,
)

heif_image.save("image.jpg", quality=100)
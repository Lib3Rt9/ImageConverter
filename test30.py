import os
from PIL import Image
import pillow_heif
from pillow_heif import register_heif_opener
import pathlib
import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog

directory = pathlib.Path(__file__).parent.resolve()
img_exts = (".HEIC", ".heic", ".HEIF", ".heif", ".JPG", ".jpg", ".PNG", ".png", ".WEBP", ".webp")
source_format = (".HEIC", ".heic", ".HEIF", ".heif")
target_format = (".jpg")
register_heif_opener()
remove_originals = True

def convert_to_heic(img_path):
    img = Image.open(img_path)
    img.show()
    heif_img = pillow_heif.from_pil_image(img)
    heif_img.save(img_path.replace(os.path.splitext(img_path)[1], target_format))

def convert_to_other(img_path):
    img = Image.open(img_path)
    img.show()
    img.save(img_path.replace(os.path.splitext(img_path)[1], target_format))

def convert_images():
    global directory, source_format, target_format
    directory = filedialog.askdirectory()
    source_format = source_entry.get()
    target_format = target_entry.get()
    for filename in os.listdir(directory):
        if filename.endswith(source_format):
            img_path = os.path.join(directory, filename)
            if target_format in (".HEIC", ".heic", ".HEIF", ".heic"):
                convert_to_heic(img_path)
            else:
                convert_to_other(img_path)
            if remove_originals:
                os.remove(img_path)

root = tk.Tk()
root.title("Image Converter")

label1 = tk.Label(root, text="Select source directory:")
label1.pack()

label2 = tk.Label(root, text="Enter source extension:")
label2.pack()

source_entry = tk.Entry(root)
source_entry.pack()

label3 = tk.Label(root, text="Enter target extension:")
label3.pack()

target_entry = tk.Entry(root)
target_entry.pack()

button = tk.Button(root, text="Convert Images", command=convert_images)
button.pack()

root.mainloop()
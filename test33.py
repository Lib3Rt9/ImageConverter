import os
from PIL import Image
import pillow_heif
from pillow_heif import register_heif_opener
import pathlib
import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

directory = pathlib.Path(__file__).parent.resolve()
img_exts = (".HEIC", ".heic", ".HEIF", ".heif", ".JPG", ".jpg", ".PNG", ".png", ".WEBP", ".webp")
source_format = (".HEIC", ".heic", ".HEIF", ".heif")
target_format = (".jpg")
register_heif_opener()
remove_originals = True

def convert_to_heic(img_path):
    img = Image.open(img_path)
    img.show()
    # heif_img = pillow_heif.from_pil_image(img)
    img.save(img_path.replace(os.path.splitext(img_path)[1], target_format))

def convert_to_other(img_path):
    img = Image.open(img_path)
    img.show()
    img.save(img_path.replace(os.path.splitext(img_path)[1], target_format))

def update_progress():
    progress['value'] += 10
    if progress['value'] < 100:
        root.after(100, update_progress)

def convert_images():
    global directory, source_format, target_format
    directory = filedialog.askdirectory()
    source_format = source_var.get()
    target_format = target_var.get()
    progress['value'] = 0
    update_progress()
    for filename in os.listdir(directory):
        if filename.endswith(source_format):
            img_path = os.path.join(directory, filename)
            if target_format in (".HEIC", ".heic", ".HEIF", ".heic"):
                convert_to_heic(img_path)
            else:
                convert_to_other(img_path)
            if remove_originals:
                os.remove(img_path)
    progress['value'] = 100

root = tk.Tk()
root.title("Image Converter")

label1 = tk.Label(root, text="Select source directory:")
label1.pack()

label2 = tk.Label(root, text="Choose source extension:")
label2.pack()

source_var = tk.StringVar(root)
source_var.set(".HEIC")

source_options = [".HEIC", ".WEBP", ".webp", "PNG", ".png", ".jpg"]
source_menu = tk.OptionMenu(root, source_var, *source_options)
source_menu.pack()

label3 = tk.Label(root, text="Choose target extension:")
label3.pack()

target_var = tk.StringVar(root)
target_var.set(".jpg")

target_options = [".HEIC", ".webp", ".png", ".jpg"]
target_menu = tk.OptionMenu(root, target_var, *target_options)
target_menu.pack()

button = tk.Button(root, text="Convert Images", command=convert_images)
button.pack()

progress = ttk.Progressbar(root, orient=tk.HORIZONTAL, length=200, mode='determinate')
progress.pack()

root.mainloop()
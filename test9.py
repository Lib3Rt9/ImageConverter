import os
from tkinter import Tk, filedialog, Button
from PIL import Image
import pillow_heif

def select_directory():
    directory = filedialog.askdirectory()
    if directory:
        convert_images(directory)

def convert_images(directory):
    extensions = (".HEIC", ".heic")
    for filename in os.listdir(directory):
        if filename.endswith(extensions):
            heif_file = os.path.join(directory, filename)
            heif_image = pillow_heif.HeifFile(heif_file)
            jpg_filename = filename
            for extension in extensions:
                jpg_filename = jpg_filename.replace(extension, ".JPG")
            jpg_file = os.path.join(directory, jpg_filename)
            heif_image.save(jpg_file, quality=100)

root = Tk()
root.title("HEIC to JPG Converter")

select_button = Button(root, text="Select Directory", command=select_directory)
select_button.pack()

root.mainloop()
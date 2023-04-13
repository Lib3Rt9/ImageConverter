import os
from tkinter import Tk, filedialog, Button, Label, Canvas
from PIL import Image
import pillow_heif

def select_directory():
    directory = filedialog.askdirectory()
    if directory:
        progress_label.config(text="Converting images...")
        progress_bar.coords(progress_rect, 0, 0, 0, 20)
        root.update()
        convert_images(directory)
        progress_label.config(text="Conversion complete!")

def convert_images(directory):
    extensions = (".HEIC", ".heic")
    files = [f for f in os.listdir(directory) if f.endswith(extensions)]
    for i, filename in enumerate(files):
        heif_file = os.path.join(directory, filename)
        heif_image = pillow_heif.HeifFile(heif_file)
        jpg_filename = filename
        for extension in extensions:
            jpg_filename = jpg_filename.replace(extension, ".JPG")
        jpg_file = os.path.join(directory, jpg_filename)
        heif_image.save(jpg_file, quality=100)
        progress = (i + 1) / len(files) * 200
        progress_bar.coords(progress_rect, 0, 0, progress, 20)
        root.update()

root = Tk()
root.title("HEIC to JPG Converter")

select_button = Button(root, text="Select Directory", command=select_directory)
select_button.pack()

progress_label = Label(root, text="")
progress_label.pack()

progress_bar = Canvas(root, width=200, height=20)
progress_bar.pack()
progress_rect = progress_bar.create_rectangle(0, 0, 0, 20, fill="green")

root.mainloop()
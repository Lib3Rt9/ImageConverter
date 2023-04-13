import os
from tkinter import Tk, filedialog, Button, Label, Canvas
from PIL import Image

def select_directory():
    directory = filedialog.askdirectory()
    if directory:
        progress_label.config(text="Converting images...")
        progress_bar.coords(progress_rect, 0, 0, 0, 20)
        root.update()
        convert_images(directory)
        progress_label.config(text="Conversion complete!")

def convert_images(directory):
    for filename in os.listdir(directory):
        name, ext = os.path.splitext(filename)
        if ext.lower() in (".jpg", ".jpeg"):
            convert_image(directory, filename, name + ".png")
            convert_image(directory, filename, name + ".webp")
        elif ext.lower() == ".png":
            convert_image(directory, filename, name + ".jpg")
            convert_image(directory, filename, name + ".webp")
        elif ext.lower() == ".webp":
            convert_image(directory, filename, name + ".jpg")
            convert_image(directory, filename, name + ".png")

def convert_image(directory, filename, new_filename):
    image = Image.open(os.path.join(directory, filename))
    image.save(os.path.join(directory, new_filename))
    progress_bar.coords(1)
    root.update()

root = Tk()
root.title("Image Converter")

select_button = Button(root, text="Select Directory", command=select_directory)
select_button.pack()

progress_label = Label(root, text="")
progress_label.pack()

progress_bar = Canvas(root, width=200, height=20)
progress_bar.pack()
progress_rect = progress_bar.create_rectangle(0, 0, 0, 20, fill="green")

root.mainloop()
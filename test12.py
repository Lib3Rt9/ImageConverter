import os
from tkinter import Tk, filedialog, Button, Label, Canvas, Listbox
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
    files = os.listdir(directory)
    target_ext = target_listbox.get(target_listbox.curselection())
    for i, filename in enumerate(files):
        name, ext = os.path.splitext(filename)
        if ext.lower() != target_ext.lower():
            convert_image(directory, filename, name + target_ext)
        progress = (i + 1) / len(files) * 200
        progress_bar.coords(progress_rect, 0, 0, progress, 20)
        root.update()

def convert_image(directory, filename, new_filename):
    image = Image.open(os.path.join(directory, filename))
    image.save(os.path.join(directory, new_filename))

root = Tk()
root.title("Image Converter")

select_button = Button(root, text="Select Directory", command=select_directory)
select_button.pack()

target_label = Label(root, text="Select target extension:")
target_label.pack()

target_listbox = Listbox(root)
target_listbox.insert(1, ".jpg")
target_listbox.insert(2, ".png")
target_listbox.insert(3, ".webp")
target_listbox.pack()

progress_label = Label(root, text="")
progress_label.pack()

progress_bar = Canvas(root, width=200, height=20)
progress_bar.pack()
progress_rect = progress_bar.create_rectangle(0, 0, 0, 20, fill="green")

root.mainloop()
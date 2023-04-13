
import os
from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image

def convert_images(var):
    dir_path = filedialog.askdirectory()
    save_ext = var.get()
    file_names = os.listdir(dir_path)
    for i, file_name in enumerate(file_names):
        file_path = os.path.join(dir_path, file_name)
        if os.path.isfile(file_path):
            img = Image.open(file_path)
            save_path = os.path.join(dir_path, f'{os.path.splitext(file_name)[0]}.{save_ext}')
            img.save(save_path)
            os.remove(file_path)
    messagebox.showinfo('Conversion Complete', 'All images have been converted.')

root = Tk()
var = StringVar(root)
var.set('png')
option_menu = OptionMenu(root, var, 'png', 'jpg', 'webp')
option_menu.pack()
Button(root, text='Convert Images', command=lambda: convert_images(var)).pack()
root.mainloop()
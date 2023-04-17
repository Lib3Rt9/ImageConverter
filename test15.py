import os
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Progressbar
from PIL import Image

def convert_images(var, progress):
    dir_path = filedialog.askdirectory()
    save_ext = var.get()
    file_names = os.listdir(dir_path)
    progress['maximum'] = len(file_names)
    for i, file_name in enumerate(file_names):
        file_path = os.path.join(dir_path, file_name)
        if os.path.isfile(file_path):
            img = Image.open(file_path)
            save_path = os.path.join(dir_path, f'{os.path.splitext(file_name)[0]}.{save_ext}')
            img.save(save_path)
            os.remove(file_path)
        progress['value'] = i + 1
        progress.update()

root = Tk()
var = StringVar(root)
var.set('png')
option_menu = OptionMenu(root, var, 'png', 'jpg', 'webp')
option_menu.pack()
progress = Progressbar(root)
progress.pack()
Button(root, text='Convert Images', command=lambda: convert_images(var, progress)).pack()
root.mainloop()
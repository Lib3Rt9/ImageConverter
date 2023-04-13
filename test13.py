import os
from tkinter import *
from tkinter import filedialog
from PIL import Image

def convert_image(var):
    file_path = filedialog.askopenfilename()
    img = Image.open(file_path)
    save_ext = var.get()
    save_path = filedialog.asksaveasfilename(defaultextension=f'.{save_ext}')
    img.save(save_path)
    os.remove(file_path)

root = Tk()
var = StringVar(root)
var.set('png')
option_menu = OptionMenu(root, var, 'png', 'jpg', 'webp')
option_menu.pack()
Button(root, text='Convert Image', command=lambda: convert_image(var)).pack()
root.mainloop()
import os
from tkinter import *
from tkinter import filedialog
from PIL import Image

def convert_images(var, canvas):
    dir_path = filedialog.askdirectory()
    print(f'Selected directory: {dir_path}')
    save_ext = var.get()
    print(f'Selected format: {save_ext}')
    file_names = os.listdir(dir_path)
    print(f'Found {len(file_names)} files in directory')
    canvas.delete('all')
    canvas.create_rectangle(0, 0, 300, 50, fill='white')
    for i, file_name in enumerate(file_names):
        print(f'Converting file {i + 1} of {len(file_names)}: {file_name}')
        file_path = os.path.join(dir_path, file_name)
        if os.path.isfile(file_path):
            try:
                img = Image.open(file_path)
                save_path = os.path.join(dir_path, f'{os.path.splitext(file_name)[0]}.{save_ext}')
                print(f'Saving converted image to: {save_path}')
                img.save(save_path)
            except Exception as e:
                print(f'Error converting {file_name}: {e}')
        progress = (i + 1) / len(file_names)
        canvas.delete('progress')
        canvas.create_rectangle(0, 0, progress * 300, 25, fill='green', tags='progress')
        canvas.delete('percentage')
        canvas.create_text(150, 12, text=f'{int(progress * 100)}%', tags='percentage')
        canvas.delete('file_name')
        canvas.create_text(150, 37, text=f'Converting {file_name}...', tags='file_name')
        root.update_idletasks()
    canvas.delete('file_name')
    canvas.create_text(150, 37, text='All images have been converted.')
    print('Conversion complete')

root = Tk()
var = StringVar(root)
var.set('png')
option_menu = OptionMenu(root, var, 'png', 'jpg', 'webp')
option_menu.pack()
canvas = Canvas(root, width=300, height=50)
canvas.pack()
Button(root, text='Convert Images', command=lambda: convert_images(var, canvas)).pack()
root.mainloop()
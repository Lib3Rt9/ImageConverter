import tkinter as tk
from tkinter import filedialog
from PIL import Image
from pillow_heif import register_heif_opener

register_heif_opener()

def convert_file():
    file_path = filedialog.askopenfilename(filetypes=[("HEIC files", "*.heic")])
    if file_path:
        im = Image.open(file_path)
        im.save(file_path.replace(".heic", ".jpg"))
        label.config(text="File converted successfully!")

root = tk.Tk()
root.title("HEIC to JPG Converter")

label = tk.Label(root, text="Select a HEIC file to convert")
label.pack()

button = tk.Button(root, text="Select File", command=convert_file)
button.pack()

root.mainloop()
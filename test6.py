import tkinter as tk
from tkinter import filedialog
from PIL import Image
import pillow_heif

def select_file():
    file_path = filedialog.askopenfilename(filetypes=[('HEIC Files', '*.heic')])
    if file_path:
        # Open the HEIC image using pillow_heif
        heif_image = pillow_heif.open_heif(file_path)
        # Save the image as a JPG with a high quality setting
        heif_image.save(file_path.replace('.HEIC', '.jpg'), quality=100)
        # Display a success message
        success_label.config(text='Image converted successfully!')

# Create the main window
root = tk.Tk()
root.title('HEIC to JPG Converter')

# Create a button for selecting a file
select_button = tk.Button(root, text='Select HEIC File', command=select_file)
select_button.pack()

# Create a label for displaying success messages
success_label = tk.Label(root, text='')
success_label.pack()

# Run the main loop
root.mainloop()
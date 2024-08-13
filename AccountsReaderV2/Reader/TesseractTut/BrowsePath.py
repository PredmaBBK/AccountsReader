import tkinter as tk
from tkinter import filedialog

def select_folder():
    # Create a root window and hide it
    root = tk.Tk()
    root.withdraw()
    
    # Open the folder selection dialog
    folder_path = filedialog.askdirectory()
    
    # Destroy the root window
    root.destroy()
    
    return folder_path

def select_file():
    # Create a root window and hide it
    root = tk.Tk()
    root.withdraw()
    
    # Open the file selection dialog
    file_path = filedialog.askopenfilename()
    
    # Destroy the root window
    root.destroy()
    
    return file_path
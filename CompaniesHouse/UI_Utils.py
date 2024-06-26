import tkinter as tk
from tkinter import ttk
import os



# This function centres the tkinter interface on the user's screen.
def center_window(window):

    # Calculate the desired dimensions (half the screen's width and height)
    width = window.winfo_screenwidth()//2
    height = window.winfo_screenheight()//2

    # Get the screen's width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    
    # Calculate the position for the window to be centered
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    
    # Set the dimensions and position of the window
    window.geometry(f"{width}x{height}+{x}+{y}")



def delete_files_in_directory(directory):
    # Check if the directory exists
    if not os.path.exists(directory):
        print(f"The directory {directory} does not exist.")
        return

    # Loop through all files in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        # Check if the path is a file
        if os.path.isfile(file_path):
            try:
                # Delete the file
                os.remove(file_path)
                print(f"Deleted file: {file_path}")
            except Exception as e:
                print(f"Failed to delete {file_path}. Reason: {e}")




def find_frames(root):
    frames = []

    def recursive_search(widget):
        # If the widget is a frame, add it to the list
        if isinstance(widget, (tk.Frame, ttk.Frame)):
            frames.append(widget)
        # Recursively search in all child widgets
        for child in widget.winfo_children():
            recursive_search(child)
    
    # Start the search from the root window
    recursive_search(root)
    
    return frames



def destroy_frames(root):
    def recursive_destroy(widget):
        # If the widget is a frame, destroy it
        if isinstance(widget, (tk.Frame, ttk.Frame)):
            widget.destroy()
        # Recursively process all child widgets
        else:
            for child in widget.winfo_children():
                recursive_destroy(child)

    # Start the destruction process from the root window
    recursive_destroy(root)
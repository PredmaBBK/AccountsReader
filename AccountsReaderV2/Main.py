import tkinter as tk
import UI_Utils as UU
import Frame1
import GlobalVars as GV

# Create the main window
root = tk.Tk()
GV.set_root_window(root)

# Set the window's title
root.title("Accounts Reader")

# Center the window
UU.center_window(root)

# Assign the initial objects (search bar and search button) to the Tkinter window in frame1
Frame1.Frame1(root)

# Start the Tkinter event loop
root.mainloop()

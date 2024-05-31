# The user interface for the account reader program. 
# This includes the search engine which connects with the Companies House search engine and returns the top relevant companies to the search. 
# Additional options to filter the companies can be added to this. 

from tkinter import *
from tkinter import ttk

# Set up the main window
root = Tk()
root.title("Accounts Reader")

# Configuring the main window's grid
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Add the main frame where the user input will be entered and results displayed
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

# Add a label to the top of the window
label = Label(root, text="This program allows you to extract the data of a company from Companies House")
label.grid(column=0, row=0, columnspan=2, sticky=(W, E), pady=10)

# Expand the mainframe with the window
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

# Start the Tkinter event loop
root.mainloop()








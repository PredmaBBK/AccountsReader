# The user interface for the account reader program. 
# This includes the search engine which connects with the Companies House search engine and returns the top relevant companies to the search. 
# Additional options to filter the companies can be added to this. 

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Scraper.scraper import company_search_results

# Set up the main window
root = Tk()
root.title("Accounts Reader")

# Add the main frame where the user input will be entered and results displayed
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

# Configuring the main window's grid
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Expand the mainframe with the window
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

# Add a label to the top of the window
label = Label(root, text="This program allows you to extract the data of a company from Companies House")
label.grid(column=0, row=0, columnspan=2, sticky=(W, E), pady=10)

# Add the search box
search_entry = Entry(root, width=50, fg='grey')
search_entry.grid(column=0, row=1, columnspan=2, padx=10, pady=10)

# Add the placeholder text functionality
# Function to handle the search action

def search_action():
    search_query = search_entry.get()
    if search_query == '' or search_query == 'Enter a company name here':
        messagebox.showwarning("Input Error", "Please enter a valid company name.")
    else:
        companies = company_search_results(search_query)
        if companies:
            display_companies(companies)
        else:
            messagebox.showinfo("No Results", "No companies found for the search query.")
    

# Function to clear the placeholder text when the entry box is clicked
def on_entry_click(event):
    if search_entry.get() == 'Enter a company name here':
        search_entry.delete(0, "end")  # delete all the text in the entry
        search_entry.insert(0, '')  # insert blank for user input
        search_entry.config(fg='black')

# Function to add the placeholder text if the entry box is empty
def on_focus_out(event):
    if search_entry.get() == '':
        search_entry.insert(0, 'Enter a company name here')
        search_entry.config(fg='grey')

# Create and place the search entry using grid
search_entry.insert(0, 'Enter a company name here')
search_entry.bind('<FocusIn>', on_entry_click)
search_entry.bind('<FocusOut>', on_focus_out)

search_button = Button(root, text="Search", command=search_action)
search_button.grid(row=1, column=1, padx=10, pady=10)

# Display the companies for the user to select from
def display_companies(companies):

    #Create the frame for the checkboxes
    frame = Frame(root)
    frame.grid(row=2, column=0, padx=10, pady=10)

    for company in companies:
        var = IntVar()
        chk = Checkbutton(frame, text=company[0], variable=var)
        chk.pack(anchor='w')






# Start the Tkinter event loop
root.mainloop()








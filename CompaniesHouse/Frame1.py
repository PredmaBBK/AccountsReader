from tkinter import ttk, N, W, E, S, Label, Entry, messagebox
from tkinter import Button, Checkbutton, IntVar, Frame, filedialog
import Scraper.scraper as scraper
import os
import UI_Utils as UU
import GlobalVars as GV
import Frame2

def Frame1(root_window):

    #test
    rootName = GV.get_root_window().title
    print(rootName)
    

    frame1 = Frame(root_window)
    frame1.grid(column=0, row=0, sticky=(N, W, E, S))

    # Configuring the main window's grid
    root_window.columnconfigure(0, weight=1)
    root_window.rowconfigure(0, weight=1)

    # Expand the mainframe with the window
    frame1.columnconfigure(0, weight=1)
    frame1.rowconfigure(0, weight=1)

    # Add a label to the top of the window
    label = Label(frame1, text="This program allows you to extract the data of a company from Companies House")
    label.grid(column=0, row=0, columnspan=2, sticky=(W, E), pady=10)

    # Add the search box
    search_entry = Entry(root_window, width=50, fg='grey')
    search_entry.grid(column=0, row=1, columnspan=2, padx=10, pady=10)

    # Add the placeholder text functionality
    # Function to handle the search action

    def search_action():
        search_query = search_entry.get()

        if search_query == '' or search_query == 'Enter a company name here':
            messagebox.showwarning("Input Error", "Please enter a valid company name.")
        else:
            companies = scraper.company_search_results(search_query)
            if companies:
                display_companies(companies, root_window)
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
    
    # Create and place the search entry, button and selection button using grid
    search_entry.insert(0, 'Enter a company name here')
    search_entry.bind('<FocusIn>', on_entry_click)
    search_entry.bind('<FocusOut>', on_focus_out)
    search_button = Button(root_window, text="Search", command=search_action)
    search_button.grid(row=1, column=1, padx=10, pady=10)




# This section of functions defines the displaying of the company checkboxes
# And the subsequent downloading of selected companies
    checkbox_vars =[]
# Function to download the selected companies
    def company_PDFs(event=None):
        selected_companies = [(var, name, link) for var, name, link in checkbox_vars if var.get() == 1]  # Extract only selected companies
        
        # Debug print to check the state of checkbox_vars
        print("checkbox_vars:", [(var.get(), name, link) for var, name, link in checkbox_vars])
        
        # The user selects the folder in which they want local files to be saved.
        file_location = ""
        while not file_location:
            file_location = save_file_dialog()
        
        # We create a temporary folder to store the PDFs, and delete any files that are currently in there
        file_location = file_location + "/tempPDFS"
        print(file_location)
        if(not os.path.isdir(file_location)):
            os.mkdir(file_location)
        
        UU.delete_files_in_directory(file_location)

        if not selected_companies:
            messagebox.showerror("Error", "Please select a company")
        else:
            print("printing selected companies: \n")
            print(selected_companies)
            for var, name, link in selected_companies:
                print(link)
                links = scraper.company_download_links(link, name, file_location)
                print(links)
        print("Moving to frame 2")
        Frame2.frame2(root_window)

# Display the companies for the user to select from
    def display_companies(companies, master):
        
        clear_checkboxes(checkbox_frame)

        for company in companies:
            var = IntVar(master)
            chk = Checkbutton(checkbox_frame, text=company[0], variable=var)
            chk.pack(anchor='w')
            checkbox_vars.append((var, company[0], company[1]))


    # Function to clear all checkboxes in the given frame
    def clear_checkboxes(frame):
        for widget in frame.winfo_children():
            widget.destroy()

    # Function to get the user to select a filesave location
    def save_file_dialog():
        file_location = filedialog.askdirectory(title="Select a folder")
        return file_location   

    # Create the frame for the checkboxes
    checkbox_frame = Frame(root_window)
    checkbox_frame.grid(row=2, column=0, padx=10, pady=10)

    selection_button = Button(root_window, text="Select companies")
    selection_button.grid(row=2, column=1, padx=10, pady=10)
    selection_button.bind("<Button-1>", lambda event: company_PDFs(event))

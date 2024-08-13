# This file is for setting the global variables needed throughout the program such as
#   - The file location that the user selects where all the temporary storage is kept
#   - The file locations of the saved PDFs



local_PDF_links = []

def append_local_PDF_links(links):
    global local_PDF_links
    local_PDF_links = local_PDF_links + links

def get_local_PDF_links():
    return local_PDF_links


top_storage_folder = ""

def set_top_storage_folder(save_location):
    global top_storage_folder
    top_storage_folder = save_location

def get_top_storage_folder():
    return top_storage_folder

root_window = ""

def set_root_window(root):
    global root_window
    root_window = root

def get_root_window():
    return root_window
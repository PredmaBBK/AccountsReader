# This file defines the functionality that converts the PDFs to images and saves it in another folder.

import fitz  # PyMuPDF
import GlobalVars
import os
import re

pdf_paths = []
storage_location = ""

def PDFtoImages():
    global pdf_paths
    pdf_paths = GlobalVars.get_local_PDF_links

    global storage_location
    storage_location = os.path.dirname(GlobalVars.get_top_storage_folder)
    image_storage_folder = "imageFromPDF"
    save_location = os.path.join(storage_location, image_storage_folder)
    print(save_location)

    for pdf_path in pdf_paths:
        try:
            pdf_document = fitz.open(pdf_path)

            # Extract company name and year
            company_year = extract_company_year(pdf_path)

            print("PDF loaded successfully")

            # Iterate through each page
            for page_num in range(len(pdf_document)):
                page = pdf_document.load_page(page_num)  # Load the page
                pix = page.get_pixmap()  # Render page to an image

                # Save the image
                output_image_path = f"{save_location}\\{company_year}_page_{page_num + 1}.png"
                pix.save(output_image_path)
                print(f"Saved page {page_num + 1} as image {output_image_path}")

        except Exception as e:
            print(f"Error processing PDF: {e}")


def extract_company_year(file_path):
    # Extract the filename from the path
    file_name = os.path.basename(file_path)

    # Use regular expression to extract the company name and year
    match = re.search(r'([^\\]+)\d{4}\.pdf$', file_path)
    
    if match:
        company_year = match.group(1)
        return company_year
    else:
        return None
import fitz  # PyMuPDF

pdf_path = "C:\\Users\\predm\\Documents\\Birkbeck\\MSc Project\\3) Analysis\\Datasets\\Thames Water Accounts PDFs\\TMS_2023.pdf"
output_folder = "C:\\Users\\predm\\Documents\\Birkbeck\\MSc Project\\3) Analysis\\Datasets\\Images"


def PDFtoImage(pdf_path, output_folder):
    # Open the PDF file
    try:
        pdf_document = fitz.open(pdf_path)
        print("PDF loaded successfully")

        # Iterate through each page
        for page_num in range(len(pdf_document)):
            page = pdf_document.load_page(page_num)  # Load the page
            pix = page.get_pixmap()  # Render page to an image

            # Save the image
            output_image_path = f"{output_folder}\\page_{page_num + 1}.png"
            pix.save(output_image_path)
            print(f"Saved page {page_num + 1} as image {output_image_path}")

    except Exception as e:
        print(f"Error processing PDF: {e}")


PDFtoImage(pdf_path, output_folder)
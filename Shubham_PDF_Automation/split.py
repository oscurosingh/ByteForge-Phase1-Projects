from PyPDF2 import PdfReader,PdfWriter
from io import BytesIO
from utils import save_file_to_temp, generate_unique_filename, log_action

def parse_page_ranges(page_range):
    '''
    Parses a string of page ranges into a set of individual page numbers.
    Args:
        page_range (str): A string containing page ranges (e.g., "1-3,5,7-9").
        Returns:
        set: A set of individual page numbers.
    '''
    pages=set()
    for part in page_range.split(','):
        if '-' in part:
            start ,end =map(int,part.split('-'))
            pages.update(range(start-1, end))
        else:
            pages.add(int(part)-1)
    return pages

def split_pdf(uploaded_file, page_range):
    """
    Splits the uploaded PDF based on user-defined page ranges.

    Args:
        uploaded_file: InMemoryUploadedFile from Streamlit
        page_range: str (e.g., '1-3,5')

    Returns:
        tuple: (BytesIO object of split PDF, generated filename)
    """
    
    temp_path = save_file_to_temp(uploaded_file)  # Save the uploaded file to a temporary location
    reader= PdfReader(temp_path)  # Read the PDF file using PdfReader
    writer = PdfWriter()  # Create a PdfWriter object to write the split PDF
    try:
        pages_to_keep = parse_page_ranges(page_range)  # Parse the page ranges into a set of individual page numbers
    except ValueError as e:
        raise ValueError(f"Invalid page range format: {e}")
    for page_num in pages_to_keep:
        if 0<= page_num < len(reader.pages):
            writer.add_page(reader.pages[page_num])
    output_pdf = BytesIO()  # Create a BytesIO object to hold the split PDF
    writer.write(output_pdf)  # Write the split PDF to the BytesIO object
    output_pdf.seek(0)  # Reset the BytesIO object pointer to the start     
    
    filename = generate_unique_filename('split.pdf')  # Generate a unique filename for the split PDF
    log_action('split_pdf',f'split PDF into {filename} with pages {page_range}')  # Log the action
    return output_pdf, filename  # Return the BytesIO object and the generated filename
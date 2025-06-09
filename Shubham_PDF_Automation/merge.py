from io import BytesIO
from PyPDF2 import PdfMerger
from utils import save_file_to_temp,generate_unique_filename, log_action


def merge_pdfs(uploaded_files):
    """
    Merges multiple uploaded PDF files into a single PDF.

    Args:
        uploaded_files (list): List of uploaded InMemoryUploadedFile objects from Streamlit.

    Returns:
        tuple: (BytesIO object of merged PDF, generated filename)
    """
    merger= PdfMerger()
    temp_paths=[]
    
    for file in uploaded_files:
        temp_path=save_file_to_temp(file)# Save the uploaded file to a temporary location
        temp_paths.append(temp_path)  # Store the temporary file path
        merger.append(temp_path)  # Append the temporary file to the merger
        
    #store the merged PDF in a BytesIO object
    merged_pdf_bytes = BytesIO() # Create a BytesIO object to hold the merged PDF
    merger.write(merged_pdf_bytes)  # Write the merged PDF to the BytesIO object
    merged_pdf_bytes.seek(0)  # Reset the BytesIO object pointer to the start
    merger.close()  # Close the merger to free resources  
    
    
    filename=generate_unique_filename('merged.pdf')  # Generate a unique filename for the merged PDF
    log_action('merge_pdfs',f'merged {len(uploaded_files)} PDFs into {filename}')  # Log the action
    return merged_pdf_bytes, filename  # Return the BytesIO object and the generated filename
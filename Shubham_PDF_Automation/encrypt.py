from PyPDF2 import PdfWriter , PdfReader
from io import BytesIO
from utils import save_file_to_temp,generate_unique_filename,log_action

def encrypt_pdf(uploaded_file, password):
    """
    Encrypts a PDF file with the specified password.

    Args:
        uploaded_file: Streamlit file uploader object (PDF)
        password: Password string to encrypt the PDF

    Returns:
        tuple: (BytesIO object of encrypted PDF, generated filename)
    """
    if uploaded_file is None or password is None:
        raise ValueError("Both uploaded file and password must be provided.")
    temp_path = save_file_to_temp(uploaded_file)  # Save the uploaded file to a temporary location
    reader = PdfReader(temp_path)  # Read the PDF file using PdfReader
    writer = PdfWriter()  # Create a PdfWriter object to write the encrypted PDF
    for page in reader.pages:
        writer.add_page(page)
        
    writer.encrypt(password)  # Encrypt the PDF with the provided password
    encrypted_pdf = BytesIO()  # Create a BytesIO object to hold the encrypted PDF
    writer.write(encrypted_pdf)  # Write the encrypted PDF to the BytesIO object
    encrypted_pdf.seek(0)  # Reset the BytesIO object pointer to the start
    
    filename = generate_unique_filename('encrypted.pdf')  # Generate a unique filename for the encrypted PDF
    log_action('encrypt_pdf', f'encrypted PDF with password for {filename}')  # Log the action  
    return encrypted_pdf, filename  # Return the BytesIO object and the generated filename
    

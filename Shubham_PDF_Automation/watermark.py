from PyPDF2 import PdfWriter, PdfReader
from io import BytesIO
from utils import save_file_to_temp, generate_unique_filename, log_action
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def create_watermark(text):
    '''
    Creates a PDF with a watermark text.
    Args:
        text (str): The watermark text to be added.
    '''
    packet = BytesIO() # Create a BytesIO object to hold the PDF data
    can = canvas.Canvas(packet, pagesize=letter) # Create a canvas to draw the watermark
    can.setFont("Helvetica", 100) # Set the font and size for the watermark text
    can.setFillAlpha(0.3) # Set the transparency of the watermark text
    can.drawCentredString(300, 400, text) # Draw the watermark text at the center of the page
    can.save() # Save the canvas to the BytesIO object
    packet.seek(0) # Reset the BytesIO object pointer to the start
    return PdfReader(packet) # Create a PdfReader object from the BytesIO object containing the watermark PDF
 
def add_watermark(pdf_file, watermark_text):
    '''
    Adds a watermark to each page of the uploaded PDF file. 
    Args:
        pdf_file: InMemoryUploadedFile from Streamlit
        watermark_text: str, the text to be used as a watermark
        Returns:
        tuple: (BytesIO object of watermarked PDF, generated filename)
    '''
    input_pdf = PdfReader(pdf_file)
    watermark_pdf = create_watermark(watermark_text) # Create a watermark PDF with the specified text
    watermark_page = watermark_pdf.pages[0] # Get the first page of the watermark PDF

    writer = PdfWriter()
    for page in input_pdf.pages:
        page.merge_page(watermark_page) # Merge the watermark page onto each page of the input PDF
        writer.add_page(page) # Add the watermarked page to the writer
 
    output = BytesIO()
    writer.write(output)
    output.seek(0)
    filename = generate_unique_filename("watermarked.pdf")
    log_action('add_watermark', f'added watermark to PDF with text: {watermark_text}')
    return output, filename
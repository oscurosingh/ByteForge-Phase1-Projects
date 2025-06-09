import streamlit as st
from utils import upload_file, validate_file 
from merge import merge_pdfs
from split import split_pdf
from watermark import add_watermark
from encrypt import encrypt_pdf
# Import necessary libraries

#set upn the page configuration
st.set_page_config(
    page_title="PDF Automation Tool",
    page_icon=":file_folder:",
    layout="wide"
)
st.title("📁 PDF Automation Tool") 
st.divider()
# Sidebar for selecting the PDF operation
st.sidebar.title("Select Operation")
operation=st.sidebar.selectbox(
    "Operation",
    options=["Choose an action:", "Merge PDFs", "Split PDF", "Add Watermark", "Encrypt PDF"  ],# "Decrypt PDF"
    key="operation"
)
#  View log file in the sidebar
if st.sidebar.checkbox("📄 View Logs"):
    try:
        with open("actions.log", "r", encoding="utf-8") as f:
            logs = f.read()
        st.sidebar.text_area("Action Logs", logs, height=350)
    except FileNotFoundError:
        st.sidebar.warning("No log file found yet.")


match operation:
    case "Merge PDFs":
        st.subheader("Merge PDFs")  
        st.info("This feature allows you to merge multiple PDF files into one.")
        files = upload_file("Upload PDF files:", key="merge", multiple=True)# key means that the file uploader will be unique for this operation
        st.divider()
        # col1, col2, col3 = st.columns([1, 2, 1])
        if st.button("Merge PDFs"): # this means that the user has clicked the button to merge PDFs
            if not files:
                st.error("Please upload at least one PDF file.")
            elif not all(validate_file(file) for file in files):
                st.error("All uploaded files must be valid PDF files.")
                st.error("Please upload valid PDF files.")
            else:
                merged_pdf,filename=merge_pdfs(files)# here merged_pdf is a BytesIO object that contains the merged PDF file, and filename is the name of the merged PDF file
                st.success(f"Successfully merged {len(files)} PDF files into {filename}.")
                st.download_button(
                    label="Download Merged PDF",
                    data=merged_pdf,
                    file_name=filename,  # Use the generated filename
                    mime="application/pdf" # Set the MIME type for PDF files(here mime means Multipurpose Internet Mail Extensions, which is a standard way of classifying file types on the internet)
                )
                
    case "Split PDF":
        st.subheader("Split PDF")
        st.info("This feature allows you to split a PDF file into multiple files.")
        pdf= upload_file("Upload PDF file to split:", key="split")  # Upload a single PDF file for splitting, here key means that the file uploader will be unique for this operation
        page = st.text_input("Enter page range (e.g. 1-3,5):", key="page_range")  # Input for page range to split the PDF
        st.divider()
        if st.button("Split PDF"):
            if not pdf:
                st.error('please upload a PDF file to split.')
            elif not validate_file(pdf):
                st.error('the uploaded file is not in PDF format.')
            elif not page:
                st.error('please enter a page range to split the pdf.')
            else:
                split_pdf, filename = split_pdf(pdf,page)  # Call the split_pdf function to split the PDF file
                st.success(f'Successfully split the PDF into {filename} with pages {page}.')
                st.download_button(
                    label = 'Download split PDF',
                    data= split_pdf,
                    file_name=filename,  # Use the generated filename
                    mime="application/pdf"  # Set the MIME type for PDF files
                )
    case "Add Watermark":
        st.subheader("Add Watermark")
        st.info("This feature allows you to add a watermark to a PDF file.")
        pdf= upload_file("Upload PDF file to add watermark:", key="watermark")  # Upload a single PDF file for adding watermark
        watermark_text = st.text_input("Enter watermark text:", key="watermark_text")  # Input for watermark text
        st.divider()
        if st.button("Add Watermark"):
            if not pdf:
                st.error("Please upload a PDF file to add a watermark.")    
            elif not validate_file(pdf):
                st.error("The uploaded file is not in PDF format.")
            elif not watermark_text:
                st.error("Please enter the watermark text.")
            else:
                watermark_pdf,filename = add_watermark(pdf,watermark_text)  # Call the add_watermark function to add watermark to the PDF file
                st.success(f'successfully added watermark to {filename}.')
                st.download_button(
                    label ='download watermarked PDF',
                    data= watermark_pdf,
                    file_name=filename,  # Use the generated filename
                    mime="application/pdf"  # Set the MIME type for PDF files
                )

    case "Encrypt PDF":
        st.subheader("Encrypt PDF")
        st.info("This feature allows you to encrypt a PDF file with a password.")
        pdf = upload_file("Upload PDF file to encrypt:", key="encrypt")  # Upload a single PDF file for encryption
        password = st.text_input("Enter password to encrypt the Pdf file :",type ="password",key='password')
        st.divider()
        if st.button('Encrypt PDF'): 
            if not pdf:
                st.error('please upload a PDF file to encrypt.')
            elif not validate_file(pdf):
                st.error('the uploaded file is not in PDF format.')
            elif not password:
                st.error('please enter a password to encrypt the PDF file.')
            else:
                encrypted_pdf , filename = encrypt_pdf(pdf, password)  # Call the encrypt_pdf function to encrypt the PDF file
                st.success(f'Successfully encrypted the PDF file as {filename}.')
                st.download_button(
                    label='Download Encrypted PDF',
                    data=encrypted_pdf,
                    file_name=filename,  # Use the generated filename
                    mime="application/pdf"  # Set the MIME type for PDF files
                )
    

   
  


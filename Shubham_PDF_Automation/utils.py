import streamlit as st
import tempfile # Temporary file handling
import os
from datetime import datetime  # For logging timestamps
import uuid  # For generating unique identifiers

# Import necessary libraries for file handling and logging

def upload_file(label, key, multiple=False):
    """
    Handles file uploads via Streamlit and returns the uploaded file(s).
    """
    if multiple:
        files = st.file_uploader(label,type='pdf',accept_multiple_files=True,key=key)
        return files
    else:
        file =st.file_uploader(label, type='pdf', key=key)  
        return file
    
def validate_file(uploaded_file):
    """
    Validates that an uploaded file is a PDF based on its filename.
    Returns True if the file has a '.pdf' extension (case-insensitive).
    """
    if uploaded_file is None:# Check if the uploaded file is None
        return False
    filename = uploaded_file.name if hasattr(uploaded_file, "name") else ""# Get the filename from the uploaded file
    _, ext = os.path.splitext(filename)# Extract the file extension
    if not ext:  # If the file has no extension, return False
        return False
    return ext.lower() == ".pdf"


def generate_unique_filename(filename):
    """
    Generates a unique filename by appending a timestamp to the original filename.
    """
    base, ext = os.path.splitext(filename)
    unique_id = uuid.uuid4().hex# Universally Unique Identifier(uuid) is a 128-bit number used to uniquely identify information in computer systems.
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")# Get the current timestamp in a specific format (YYYYMMDDHHMMSS)
    return f"{base}_{timestamp}_{unique_id}{ext}"
   

def log_action(action, details):
    """
    Logs the action in Streamlit and also saves it in a local log file.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = f"[{timestamp}] {action.upper()}: {details}"
    st.info(message)  # Display the log message in Streamlit
    # Save log to file
    LOG_FILE = "actions.log"
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'w') as f:
            f.write("Action Log\n")
            f.write("==========\n")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(message + "\n")
    
    
def save_file_to_temp(file):
    """
    Saves an uploaded file to a temporary location and returns the path.
    """
    with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as temp_file: # Create a temporary file with a .pdf suffix
        file.seek(0)  # Ensure the file pointer is at the start
        temp_file.write(file.read()) # Write the content of the uploaded file to the temporary file
        temp_file.flush()
        return temp_file.name # Returns the path to the temporary file



    
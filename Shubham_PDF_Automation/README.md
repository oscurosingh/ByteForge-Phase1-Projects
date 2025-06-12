# PDF Automation Tool

A powerful web-based PDF automation tool built with Streamlit that allows you to perform various PDF operations easily.

## Features

- **Merge PDFs**: Combine multiple PDF files into a single document
- **Split PDF**: Extract specific pages or page ranges from a PDF
- **Add Watermark**: Add text watermarks to your PDF documents
- **Encrypt PDF**: Secure your PDFs with password protection

## Installation

1. Clone this repository:
```bash
git clone <https://github.com/oscurosingh/ByteForge-Phase1-Projects/edit/main/Shubham_PDF_Automation>
cd pdf-automation
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the application:
```bash
streamlit run main.py
```

2. Open your web browser and navigate to the URL shown in the terminal (typically http://localhost:8501)

3. Use the sidebar to select the desired PDF operation:
   - **Merge PDFs**: Upload multiple PDF files and combine them
   - **Split PDF**: Upload a PDF and specify page ranges (e.g., "1-3,5")
   - **Add Watermark**: Upload a PDF and add custom watermark text
   - **Encrypt PDF**: Upload a PDF and set a password for protection

## Features in Detail

### Merge PDFs
- Upload multiple PDF files
- Files are merged in the order they are uploaded
- Download the merged PDF with a unique filename

### Split PDF
- Upload a single PDF file
- Specify page ranges using formats like "1-3,5,7-9"
- Download the extracted pages as a new PDF

### Add Watermark
- Upload a PDF file
- Enter custom watermark text
- Watermark is added with 30% opacity
- Download the watermarked PDF

### Encrypt PDF
- Upload a PDF file
- Set a password for protection
- Download the encrypted PDF

## Logging

The application maintains a log of all operations in `actions.log`. You can view the logs directly in the application's sidebar.

## Requirements

- Python 3.x
- streamlit>=1.31.1
- PyPDF2>=3.0.1
- reportlab>=4.1.0

## License

This project is open source and available under the MIT License.


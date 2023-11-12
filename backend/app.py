from flask import Flask, request, jsonify, send_file
from pdf2image import convert_from_bytes
from flask_cors import CORS
import pytesseract
import os
from PIL import Image
from tempfile import NamedTemporaryFile
import fitz

app = Flask(__name__)
CORS(app)

# Set the path to the Tesseract OCR executable
pytesseract.pytesseract.tesseract_cmd = 'backend/tesseract/5.3.3/bin/tesseract'


@app.route('/test', methods=['POST'])
def extract():
    return "hello"

@app.route('/api/extract_text', methods=['POST'])
def extract_text():
    file = request.files['file']
    if '.pdf' in file.filename:
        try:
        # Assuming you're sending a PDF file in the request
            uploaded_file = request.files['file']
        
        # Save the uploaded file
            pdf_path = 'uploaded_file.pdf'
            uploaded_file.save(pdf_path)

        # Extract text from the PDF
            text = pdf_to_text(pdf_path)
            os.remove(pdf_path)

        # with open("output.txt", 'w') as output:
        #     # Write the string to the file
        #     output.write(text)

        # return output
            return jsonify({"text": text})
    
        except Exception as e:
            return jsonify({"error": str(e)})
    else:
        try:
        # Check if the 'file_path' field is present in the request
        # for file in request.files:
        #     print(file + '\n')
            if 'file' not in request.files:
                return jsonify({'error': 'No file path provided'})

            file = request.files['file']

            allowed_extensions = {'jpg', 'jpeg', 'png'}

            if '.' not in file.filename or file.filename.rsplit('.', 1)[1].lower() not in allowed_extensions:
                return jsonify({'error': 'Invalid file format'})
        
            # Save the file to a temporary location
            with NamedTemporaryFile(delete=False, suffix=".jpg") as temp_file:
                file.save(temp_file.name)
                temp_file_path = temp_file.name

        # images = convert_from_bytes(open(temp_file_path, 'rb').read(), 500)  # Set the DPI as needed
            image = Image.open(temp_file_path)
        # Extract text using Tesseract OCR
            text = pytesseract.image_to_string(image)
            os.remove(temp_file_path)
            return jsonify({'text': text})

        # Check if the file exists
        # if not os.path.exists(file_path):
        #     return jsonify({'error': 'File not found'})

        # with open("output.txt", 'w') as output:
        #     # Write the string to the file
        #     output.write(extracted_text)

        # return output

        except Exception as e:
            return jsonify({'error': f'Error processing image: {str(e)}'})

def pdf_to_text(pdf_path):
    text = ""
    with fitz.open(pdf_path) as pdf_document:
        for page_number in range(pdf_document.page_count):
            page = pdf_document[page_number]
            text += page.get_text()

    return text

if __name__ == '__main__':
    app.run(debug=True)



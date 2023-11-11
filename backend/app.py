from flask import Flask, request, jsonify
from pdf2image import convert_from_bytes
import pytesseract
import os
from PIL import Image
from tempfile import NamedTemporaryFile

app = Flask(__name__)

# Set the path to the Tesseract OCR executable
pytesseract.pytesseract.tesseract_cmd = '/Users/kanishk/Desktop/school/madhacks-f23/backend/tesseract/5.3.3/bin/tesseract'

@app.route('/test', methods=['POST'])
def extract():
    return "hello"

@app.route('/api/extract_text', methods=['POST'])
def extract_text():
    # Check if a file is present in the request
    # print(request.files.keys)
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'})

    file = request.files['file']

    # Check if the file has an allowed extension (e.g., PDF)
    allowed_extensions = {'jpg', 'jpeg', 'png'}
    if '.' not in file.filename or file.filename.rsplit('.', 1)[1].lower() not in allowed_extensions:
        return jsonify({'error': 'Invalid file format'})

    try:
        # Save the file to a temporary location
        with NamedTemporaryFile(delete=False, suffix=".jpg") as temp_file:
            file.save(temp_file.name)
            temp_file_path = temp_file.name

        # Convert PDF to images using pdf2image
        # images = convert_from_bytes(open(temp_file_path, 'rb').read(), 500)  # Set the DPI as needed
        image = Image.open(temp_file_path)
        # Extract text using Tesseract OCR
        text = pytesseract.image_to_string(image)
        os.remove(temp_file_path)
        return jsonify({'text': text})

    except Exception as e:
        return jsonify({'error': f'Error processing PDF: {str(e)}'})

if __name__ == '__main__':
    app.run(debug=True)



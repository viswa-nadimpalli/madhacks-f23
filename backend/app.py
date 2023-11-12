from flask import Flask, request, jsonify, send_file
from pdf2image import convert_from_bytes
from flask_cors import CORS
import pytesseract
import os
from PIL import Image
from tempfile import NamedTemporaryFile
import fitz

from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI

import sys
import os

def questions(output, type):
    openai_api_key = os.getenv("OPENAI_API_KEY")

    client = OpenAI(api_key = openai_api_key)

    # with open('output.txt', 'r', encoding='utf-8') as file:
    #     content = file.read()

    # Construct a prompt
    prompt = f"Generate questions and answers based on the following text:\n{output}\n"
    # question_type = input("Enter the corresponding number of the type of question:\n1. True/False\n2. Multiple Choice\n3. Short Answer\nResponse: ")
    question_type = type
    if question_type == "1":
        prompt += "Make the questions 'True/False'. Make sure to randomize the true and falses."
    elif    question_type == "2":
        prompt += "Make the questions 'Multiple Choice'."
    elif question_type == "3":
        prompt += "Make the questions 'Short Answer'."
    else:
        print("Invalid Input")
        sys.exit(1)
    # prompt += switchQuestion(1)

    prompt += " Separate the questions and answers with a questions section, starting with 'Questions:', and an answers section, starting with 'Answers:'."

    # print(prompt + "\n\n\n")
    # print("cooking")
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "user", "content": prompt}
        ],
        model="gpt-3.5-turbo",
    )

    response_content = chat_completion.choices[0].message.content

# print(response_content + "\n")

    if "Answers:" in response_content:
        string_parts = response_content.split("Answers:", 1)

        questions = string_parts[0].strip()
        answers = "Answers:\n" + string_parts[1].strip()

        # print(questions + "\n")
        # print(answers)
        return questions + "\n" + answers

app = Flask(__name__)
CORS(app)

# Set the path to the Tesseract OCR executable
pytesseract.pytesseract.tesseract_cmd = 'backend/tesseract/5.3.3/bin/tesseract'


@app.route('/test', methods=['POST'])
def extract():
    return "hello"

@app.route('/api/extract_text/<type>', methods=['POST'])
def extract_text(type):

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
            # return text
            return questions(text, type+"") + ""
            
            
    
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
            # return text
            return questions(text, type+"")+""

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



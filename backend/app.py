from flask import Flask, request, jsonify, send_file, make_response
from pdf2image import convert_from_bytes
from flask_cors import CORS
import pytesseract
import os
from PIL import Image
from tempfile import NamedTemporaryFile
import fitz
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfgen import canvas
from atlas import dbmethods as atlas
import pymongo
import datetime

from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI

import sys
from io import BytesIO
import os

openai_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key = openai_api_key)
def questions(output, type, userID = -1):



    # if userID != -1:
    #     user = getUser.fetchUser(ID)


    # with open('output.txt', 'r', encoding='utf-8') as file:
    #     content = file.read()

    # Construct a prompt
    if type != "4":
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
        response_content = generate_responses(prompt).choices[0].message.content

    # print(response_content + "\n")

        if "Answers:" in response_content:
            string_parts = response_content.split("Answers:", 1)

            questions = string_parts[0].strip()
            answers = "Answers:\n" + string_parts[1].strip()


            # print(questions + "\n")
            # print(answers)
            # if userID != -1:
            #     client = connect.getClient()
            #     db = client.gettingStarted
            #     people = db.people
            #     x = datetime.datetime.now()
            #     dt = x.strftime("%x")+"-"+x.strftime("%X")
            #     print('This is error output', file=sys.stderr)
            #     people.update_one(
            #         { "id": userID }
            #         ,
            #         { "$set": { dt: questions + "\n" + answers } }
            #     )
                
            return questions + "\n" + answers
    else:
        prompt = f"Generate a cheat sheet based on the following text:\n{output}\n"
        response_content = generate_responses(prompt).choices[0].message.content
        print("hi")
        text_to_pdf(response_content, "cheatsheet.pdf")
        print("hello")
        return send_file("../cheatsheet.pdf", as_attachment=True)

# converts the generated text to a pdf format for cheatsheet
def text_to_pdf(text, output_path):
    doc = SimpleDocTemplate(output_path, pagesize = letter)
    
    styles = getSampleStyleSheet()
    title_style = styles['Title']
    normal_style = styles['Normal']

    story = []

    title_text = "Jotter Cheat Sheet"
    title = Paragraph(title_text, title_style)
    story.append(title)

    story.append(Spacer(1, 12))

    for paragraph in text.split('\n'):
        story.append(Paragraph(paragraph, normal_style))
        story.append(Spacer(1, 6))

    doc.build(story)

def generate_responses (prompt):
    return client.chat.completions.create(
        messages = [
            {"role": "user", "content": prompt}
        ],
        model = "gpt-3.5-turbo"
    )

app = Flask(__name__)
CORS(app)



@app.route("/mongo/add_quiz/<userID>/<quizText>", methods=["GET", "POST"])
def add_quiz(userID, quizText):
    return atlas.add_quiz(userID, quizText)


# Set the path to the Tesseract OCR executable
pytesseract.pytesseract.tesseract_cmd = 'backend/tesseract/5.3.3/bin/tesseract'

# @app.route('/generate_pdf')
# def generate_pdf():
#     text_to_pdf(response_content, "cheatsheet.pdf")

@app.route('/generate_pdf', methods=['GET'])
def generate_pdf():
    pdf_file_path = 'cheatsheet.pdf'

    with open(pdf_file_path, 'rb') as pdf_file:
        # Read the content of the existing PDF file
        pdf_content = pdf_file.read()

    # Create a BytesIO buffer and write the PDF content to it
    pdf_buffer = BytesIO(pdf_content)

    # Create a response object to send the PDF as a file
    response = send_file(
        pdf_buffer,
        download_name='output.pdf',
        as_attachment=True,
        mimetype='application/pdf'
    )

    return response


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
            return questions(text, type+"")
            
            
    
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
            return questions(text, type+"")

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
    # app.run(host='localhost', port=3001, debug=True)
    app.run(debug=True)



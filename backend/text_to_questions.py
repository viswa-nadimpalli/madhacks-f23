# import statements
from dotenv import load_dotenv
load_dotenv()
from openai import OpenAI
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import sys
import os

client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))

with open('output.txt', 'r', encoding='utf-8') as file:
    content = file.read()

prompt = ""
initial_question = input("Enter '1' for questions and '2' for a cheat sheet: ")



def generate_responses (prompt):
    return client.chat.completions.create(
        messages = [
            {"role": "user", "content": prompt}
        ],
        model = "gpt-3.5-turbo"
    )


def text_to_pdf_styled(text, output_path):
    # Create a SimpleDocTemplate
    doc = SimpleDocTemplate(output_path, pagesize=letter)
    
    # Get sample styles
    styles = getSampleStyleSheet()
    title_style = styles['Title']
    normal_style = styles['Normal']

    # Build the story with title and paragraphs
    story = []

    # Add title
    title_text = "Jotter Cheat Sheet"
    title = Paragraph(title_text, title_style)
    story.append(title)
    
    # Add space after title
    story.append(Spacer(1, 12))

    # Add paragraphs with styles
    for paragraph in text.split('\n'):
        story.append(Paragraph(paragraph, normal_style))
        # Add space between paragraphs
        story.append(Spacer(1, 6))
    
    # Build the PDF
    doc.build(story)



if initial_question == "1":
    prompt = f"Generate questions and answers based on the following text:\n{content}\n"
    question_type = input("Enter the corresponding number of the type of question:\n1. True/False\n2. Multiple Choice\n3. Short Answer\nResponse: ")

    if question_type == "1":
        prompt += "Make the questions 'True or False'. Fifty percent of the answers should be true, and fifty percent of the answers should be false."
    elif question_type == "2":
        prompt += "Make the questions 'Multiple Choice'."
    elif question_type == "3":
        prompt += "Make the questions 'Short Answer'."
    else:
        print("Invalid Input")
        sys.exit(1)
    question_amount = input("Enter the number of questions you want: ")
    prompt += f" Separate the questions and answers with a questions section, starting with 'Questions:', and an answers section, starting with 'Answers:'. Please generate {question_amount} questions."
    response_content = generate_responses(prompt).choices[0].message.content

    if "Answers:" in response_content:
        string_parts = response_content.split("Answers:", 1)

        questions = string_parts[0].strip()
        answers = "Answers:\n" + string_parts[1].strip()

        print(questions + "\n")
        print(answers)
    else:
        print("'Answers:' not found. Unexpecteed GPT-3 response")
        sys.exit(1)
elif initial_question == "2":
    prompt = f"Generate a cheat sheet based on the following text:\n{content}\nDo not start the sheet with a 'Cheat Sheet' title"
    response_content = generate_responses(prompt).choices[0].message.content
    print(response_content)
    text_to_pdf_styled(response_content, "cheatsheet.pdf")
else:
    print("Invalid Input")
    sys.exit(1)
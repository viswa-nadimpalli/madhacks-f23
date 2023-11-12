from openai import OpenAI
import sys

client = OpenAI(api_key="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")

with open('output.txt', 'r', encoding='utf-8') as file:
    content = file.read()

# Construct a prompt
prompt = f"Generate questions and answers based on the following text:\n{content}\n"
question_type = input("Enter the corresponding number of the type of question:\n1. True/False\n2. Multiple Choice\n3. Short Answer\nResponse: ")

if question_type == "1":
    prompt += "Make the questions 'True/False'. Make sure to randomize the true and falses."
elif question_type == "2":
    prompt += "Make the questions 'Multiple Choice'."
elif question_type == "3":
    prompt += "Make the questions 'Short Answer'."
else:
    print("Invalid Input")
    sys.exit(1)

prompt += " Separate the questions and answers with a questions section, starting with 'Questions:', and an answers section, starting with 'Answers:'."

print(prompt + "\n\n\n")

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

    print(questions + "\n")
    print(answers)
from gemini_secrets import api_key
from google import genai # requires pip install -q -U google-genai
import json
import pandas as pd
import os
import csv
import time 
df = pd.read_csv("question_answer_context_3B.csv")

prompt_template = (
    "Evaluate the RAG model output based on the following criteria:\n"
    "1. Relevance: Does the retrieved context relate to the question? (0 or 1)\n"
    "2. Accuracy: Is the answer factually correct? (0 or 1)\n"
    "3. Coherence: Is the answer well-formed and coherent? (0 or 1)\n"
    "Provide your evaluation as a JSON object with binary scores for each category.\n\n"
    "Context: {context}\n"
    "Question: {question}\n"
    "Answer: {answer}"
    "Make sure to respond in the correct json format."
)


def parse_gemini_response(response):
    text_content = text_content = response.candidates[0].content.parts[0].text

    json_str = text_content.split('```json\n')[1].split('\n```')[0]


    try:
        data = json.loads(json_str)
        relevance = data.get('relevance', None)
        accuracy = data.get('accuracy', None)
        coherence = data.get('coherence', None)

        return relevance, accuracy, coherence

    except json.JSONDecodeError:
        print("Ошибка при парсинге JSON.")
        return None, None, None

def test_data(df, turncate_size, prompt_template, output_file):
    """
    :param df: assumed to contain collums "questions", "answer", "contexts"
    :param turncate_size: The amount of context that will be included when querying gemini
    :param prompt_template: The prompt that the model will consider when testing
    :param output_file: The file where the results will be saved
    """
    if not os.path.exists(output_file):
        with open(output_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['question', 'answer', 'context', 'relevance', 'accuracy', 'coherence'])

    for _, row in df.iterrows():
        relevancies = []
        accuracies = []
        coherencies = []

        question = row["questions"]
        answer = row["answers"]
        context = row["contexts"]

        # split the context and answers
        tokens = context.split(" ")
        tokens = tokens[:turncate_size*2]
        context = " ".join(tokens)

        # split the context and answers
        answer = answer.split(" ")
        answer = answer[:turncate_size]
        answer = " ".join(answer)

        prompt = prompt_template.format(context=context, question=question, answer=answer)
        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model="gemini-2.0-flash", contents=prompt
        )
        relevance, accuracy, coherence = parse_gemini_response(response)
        with open(output_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([question, answer, context, relevance, accuracy, coherence])
        time.sleep(5)
        # add these to their respective columns in the output file csv. if not make a csv with these columns
        # save the progress









    print(f"Results saved to {output_file}")

test_data(df, 400, prompt_template, "3B_gemini_test_results.csv")
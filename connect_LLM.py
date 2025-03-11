from create_db import db, get_embedding_function
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.vectorstores import Chroma
import transformers
import torch
import argparse
import warnings
import sys


warnings.filterwarnings('ignore')


# Create prompt template for LLM
prompt_tmplt = """
Answer the question based on the following context, in a concise and summarized manner. Limit your response to 500 tokens or less and always finish your sentence! Make sure to format your answer so it is clear:

{context}

------
Give a concise clear answer to the question based on the above context: {question}
"""

# context is the retrieved content from the database (db)
# question is what we want to ask the LLM


# Search the database (db)
def query_rag(question):
    if torch.backends.mps.is_available():
        device = "mps"
    else:
        device = "cpu"

    print(f"Using device: {device}")

    model_id = "meta-llama/Llama-3.2-1B-Instruct"

    generator = transformers.pipeline("text-generation", model=model_id, torch_dtype=torch.bfloat16, device=device)

    # Embeds the question and searches the database
    results = db.similarity_search_with_score(question, k=3)

    # Formats the retreived documents
    context_text = "\n\n---\n\n".join([doc.page_content for doc, score in results])

    prompt_template = ChatPromptTemplate.from_template(prompt_tmplt)

    prompt = prompt_template.format(context=context_text, question=question)

    output = generator(prompt, max_new_tokens=1000, top_k=10)

    generated = output[0]["generated_text"]

    to_remove = "Give a concise clear answer to the question based on the above context:"

    ques_answer = generated.split(to_remove)[1]

    answer = ques_answer.split(question)[1]

    return answer

parser = argparse.ArgumentParser()
parser.add_argument("question", type=str, help="The question for model.")
args = parser.parse_args()
output = query_rag(args.question)

print(output)






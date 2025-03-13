from create_db import db, get_embedding_function
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.vectorstores import Chroma
import transformers
import torch
import argparse
import warnings
import sys
import pandas as pd

# Open the test file
df = pd.read_csv("RAG_test_dataset.csv")
print(df.head())

# Ensure all questions are strings and handle NaN values
df["Question"] = df["Question"].astype(str)  # Convert all to strings
df["Question"] = df["Question"].fillna("")   # Replace NaN with empty string

questions = df["Question"].tolist()
answers = []
contexts = []

# Ignore warnings
warnings.filterwarnings('ignore')
seed = 27
torch.manual_seed(seed)
torch.cuda.manual_seed_all(seed)
transformers.set_seed(seed)

# Create prompt template for LLM
prompt_tmplt = """
Answer the question based on the following context, in a concise and summarized manner. Limit your response to 300 tokens or less and always finish your sentence! Make sure to format your answer so it is clear:

{context}

------
Give a concise clear answer to the question based on the above context, limit your response to 300 tokens or less and make sure to summarize, rarely use lists: {question}
"""

# Function to query the RAG system
def query_rag(question):
    if not isinstance(question, str) or question.strip() == "":
        return "Invalid question", "No context available"

    if torch.cuda.is_available():
        device = "cuda"
    elif torch.backends.mps.is_available():
        device = "mps"
    else:
        device = "cpu"

    model_id = "meta-llama/Llama-3.2-3B-Instruct"
    generator = transformers.pipeline("text-generation", model=model_id, torch_dtype=torch.bfloat16, device=device)

    # Embeds the question and searches the database
    results = db.similarity_search_with_score(question, k=1)

    # Formats the retrieved documents
    context_text = "\n\n---\n\n".join([doc.page_content for doc, score in results])

    prompt_template = ChatPromptTemplate.from_template(prompt_tmplt)
    prompt = prompt_template.format(context=context_text, question=question)

    output = generator(prompt, max_new_tokens=1000, top_k=10)
    generated = output[0]["generated_text"]

    to_remove = "Give a concise clear answer to the question based on the above context, limit your response to 300 tokens or less and make sure to summarize, rarely use lists:"
    ques_answer = generated.split(to_remove)[1]
    answer = ques_answer.split(question)[1]

    return answer, context_text

# Process questions and store results
for question in questions:
    output, context_text = query_rag(question)
    answers.append(output)
    contexts.append(context_text)

# Save results to CSV
df = pd.DataFrame({"questions": questions, "answers": answers, "contexts": contexts})
df.to_csv("question_answer_context_2.csv", index=False)

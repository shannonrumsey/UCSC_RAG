from create_db import db, get_embedding_function
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.vectorstores import Chroma
import transformers
import torch
import argparse
import warnings
import sys
from transformers import AutoModelForCausalLM, AutoTokenizer
from textwrap import dedent

warnings.filterwarnings('ignore')
seed = 27
torch.manual_seed(seed)
torch.cuda.manual_seed_all(seed)
transformers.set_seed(seed)

sys_prompt = "Answer the user's question based on the user's context, in a concise and summarized manner. Limit your response to 300 tokens or less and always finish your sentence! Make sure the answer is concise, clear and formatted summarization. Rarely use lists".strip()
    
user_prompt = dedent("""
<question>
{question}
</question>
<context>
{context}
</context>
""").strip()

# Search the database (db)
def query_rag(question):
    if torch.backends.mps.is_available():
        device = torch.device('mps')
    elif torch.cuda.is_available():
        device = torch.device('cuda')
    else:
        device = torch.device('cpu')
    
    model_id = "meta-llama/Llama-3.1-8B-Instruct"

    generator = transformers.pipeline("text-generation", model=model_id, torch_dtype=torch.bfloat16, device=device)

    # Embeds the question and searches the database
    results = db.similarity_search_with_score(question, k=3)

    # Formats the retreived documents
    context_text = "\n\n---\n\n".join([doc.page_content for doc, score in results])

    tokenizer = AutoTokenizer.from_pretrained(model_id)
    
    messages = [
        {'role': 'system', 'content': sys_prompt},
        {'role': 'user', 'content': user_prompt.format(question=question, context=context_text)}
    ]
    
    prompt = tokenizer.apply_chat_template(messages, add_generation_prompt=True, tokenize=False)
    
    
    output = generator(prompt, max_new_tokens=1000, top_k=10)
    # print(output)
    generated = output[0]["generated_text"]

    answer = generated.split("assistant<|end_header_id|>")[1]


    return answer

parser = argparse.ArgumentParser()
parser.add_argument("question", type=str, help="The question for model.")
args = parser.parse_args()
output = query_rag(args.question)

print(output)





import os
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
embeddings = HuggingFaceEmbeddings(model_name="all-mpnet-base-v2")
import chromadb
import shutil

# Read files and create list of files
documents = []
for filename in os.listdir("scraped"):
    file_path = os.path.join("scraped", filename)
    with open(file_path, "r") as f:
        # Convert files into Document objects for langchain
        documents.append(Document(f.read()))

# Split documents into chunks
def split_documents(documents):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=400,
        chunk_overlap=100,
        length_function=len,
        is_separator_regex=False
    )
    return text_splitter.split_documents(documents)

# Convert documents into embeddings and store in Chroma database
def get_embedding_function(chunks):
    vectorstore = Chroma.from_documents(documents=chunks, embedding=embeddings)
    return vectorstore

chunks = split_documents(documents)
vectorstore = get_embedding_function(documents)
retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 6})
query = "What is needed to apply to the NLP program?"
retrieved_docs = retriever.invoke(query)
print(f"Inputs to the database: {query}")
print(f"What is fetched from the database: {retrieved_docs[0].page_content}")



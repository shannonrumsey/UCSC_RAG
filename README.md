# **UCSC RAG**

This project implements a **Retrieval-Augmented Generation (RAG) model** using **LangChain**, **ChromaDB**, and **Llama 3.2**, with data scraped from **UCSC NLP-related websites**. It allows users to **query extracted content** to get concise, context-aware responses.

---

## **1. Installation**

### **Prerequisites**

Make sure you have the following installed:

- Python **3.8+**
- Pip package manager

### **Install Dependencies**

Run the following command to install all required libraries:

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not provided, install dependencies manually:

```bash
pip install beautifulsoup4 requests langchain chromadb torch transformers
```

---

## **2. Scraping Data**

This script scrapes text from **UCSC NLP-related web pages** and stores them in a local directory.

### **Run the scraper**

```bash
python scrape.py
```

This will:

1. Download the text from specified URLs.
2. Strip out unnecessary elements like styles and scripts.
3. Save the processed text in the `scraped/` directory.

🚀 **Note:** Scraping includes a **30-second delay** per request to avoid being blocked.

---

## **3. Creating the Vector Database**

Once the text is scraped, we need to convert it into vector embeddings and store them in **ChromaDB**.

### **Run the embedding script**

```bash
python create_db.py
```

This will:

1. Load all scraped text files.
2. Split the text into smaller chunks for efficient retrieval.
3. Embed the text using **HuggingFace’s all-mpnet-base-v2** model.
4. Store the vectorized documents in **ChromaDB**.

---

## **4. Querying the RAG Model**

Once the database is set up, you can **ask questions** about the scraped content.

### **Run a query**

```bash
python query_rag.py "What is the UCSC NLP program?"
```

This will:

1. **Embed the question** and search for the most relevant context in the database.
2. **Generate a response** using **Llama-3.2-1B-Instruct**.
3. **Output a concise and formatted answer**.

---

## **5. Explanation of Main Files**

| File               | Description                                           |
| ------------------ | ----------------------------------------------------- |
| `scrape.py`        | Scrapes content from UCSC NLP-related sites.          |
| `create_db.py`     | Converts text into embeddings and stores in ChromaDB. |
| `query_rag.py`     | Queries the vector database and generates responses.  |
| `requirements.txt` | List of required dependencies.                        |

---

## **6. Notes & Troubleshooting**

### **Common Issues**

1. **Missing dependencies?**  
   Run `pip install -r requirements.txt` to install all required libraries.
2. **Model download issues?**  
   Ensure `torch` and `transformers` are installed and update them if needed:
   ```bash
   pip install --upgrade torch transformers
   ```
3. **Slow response time?**

   - Ensure that ChromaDB is running efficiently.
   - Use a **GPU** for faster LLM inference.

4. **Errors running queries?**
   - Make sure you ran `create_db.py` before `query_rag.py`.
   - If `query_rag.py` crashes, check if the database exists and is correctly populated.

---

## **7. Future Improvements**

- Improve scraper to **extract structured content** (e.g., tables, lists).
- Use a **larger LLM model** for improved response quality.
- Implement **Slack integration** for querying UCSC NLP Slack data (if permitted).

---

### **Need Help?**

If you run into any issues, feel free to reach out! 🚀

Here's the **updated README** based on the file structure in your image. I have adjusted the file names accordingly to match your project directory.

---

# **UCSC_RAG**

This project implements a **Retrieval-Augmented Generation (RAG) model** using **LangChain**, **ChromaDB**, and **Llama 3.2**. It scrapes UCSC NLP-related websites, stores text embeddings in a vector database, and allows users to query the data for contextual responses.

---

## **1. Installation**

### **Prerequisites**

Ensure you have:

- Python **3.8+**
- Pip package manager
- Virtual environment (optional but recommended)

### **Install Dependencies**

Run the following command to install required libraries:

```bash
pip install -r requirements.txt
```

If `requirements.txt` is missing, install manually:

```bash
pip install beautifulsoup4 requests langchain chromadb torch transformers
```

---

## **2. Scraping Data**

The **`scraper.py`** script extracts text from UCSC NLP-related web pages and saves it in the `scraped/` directory.

### **Run the scraper**

```bash
python scraper.py
```

This will:

1. Fetch content from predefined URLs.
2. Remove unnecessary elements (styles, scripts).
3. Save the cleaned text in the `scraped/` directory.

🚀 **Note:** The script includes a **30-second delay per request** to avoid being blocked.

---

## **3. Creating the Vector Database**

Once data is scraped, it must be converted into **vector embeddings** and stored in **ChromaDB**.

### **Run the database creation script**

```bash
python create_db.py
```

This will:

1. Load all scraped text files from `scraped/`.
2. Split text into smaller chunks.
3. Convert text into embeddings using **HuggingFace’s all-mpnet-base-v2** model.
4. Store embeddings in **ChromaDB**.

---

## **4. Querying the RAG Model**

Once the database is built, you can **ask questions** about the scraped content.

### **Run a query**

```bash
python connect_LLM.py "What is the UCSC NLP program?"
```

This will:

1. **Embed the question** and search for the most relevant content in ChromaDB.
2. **Generate a response** using **Llama-3.2-1B-Instruct**.
3. **Return a concise, formatted answer.**

---

## **5. Explanation of Main Files**

| File               | Description                                                   |
| ------------------ | ------------------------------------------------------------- |
| `scraper.py`       | Scrapes UCSC NLP-related websites.                            |
| `create_db.py`     | Converts text into embeddings and stores in ChromaDB.         |
| `connect_LLM.py`   | Queries the database and generates responses using Llama 3.2. |
| `requirements.txt` | List of required dependencies.                                |
| `.gitignore`       | Prevents tracking of unnecessary files.                       |
| `scraped/`         | Stores extracted text files.                                  |

---

## **6. Notes & Troubleshooting**

### **Common Issues**

1. **Missing dependencies?**  
   Run `pip install -r requirements.txt` to install required libraries.

2. **LLM model download issues?**  
   Ensure `torch` and `transformers` are installed:

   ```bash
   pip install --upgrade torch transformers
   ```

3. **Slow query responses?**

   - Ensure ChromaDB is running efficiently.
   - Use a **GPU** for faster LLM inference.

4. **Database not found?**
   - Ensure `create_db.py` was run **before** querying the model.
   - Check if the `scraped/` directory contains text files.

---

## **7. Future Improvements**

- Enhance the **scraper** to extract structured content (tables, lists).
- Use a **larger LLM model** for better answer quality.
- Implement **Slack integration** to extract UCSC NLP Slack data (if permitted).

---

## **8. Need Help?**

If you run into issues, feel free to reach out! 🚀

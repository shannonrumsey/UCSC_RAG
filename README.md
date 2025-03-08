Here's your **updated README** with a section about **getting permission to use Llama 3.2** and **authenticating with an access token**.

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

## **5. Getting Access to Llama 3.2**

The **Llama 3.2-1B-Instruct** model is **restricted**, and you must request access before using it.

### **Steps to Request Access:**

1. Go to the model's page on Hugging Face:  
   👉 [meta-llama/Llama-3.2-1B-Instruct](https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct)
2. Click **"Expand to review and access"** under the "LLAMA 3.2 COMMUNITY LICENSE AGREEMENT."
3. Read the terms, **check the box to agree**, and **request access**.
4. Wait for approval (you’ll receive an email once granted).

### **Authenticate with Hugging Face**

Once access is granted, log in to Hugging Face from the terminal:

```bash
huggingface-cli login
```

Enter your **Hugging Face access token** (found at [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)).

After logging in, you can **run the query script as usual**:

```bash
python connect_LLM.py "What is the UCSC NLP program?"
```

---

## **6. Explanation of Main Files**

| File               | Description                                                   |
| ------------------ | ------------------------------------------------------------- |
| `scraper.py`       | Scrapes UCSC NLP-related websites.                            |
| `create_db.py`     | Converts text into embeddings and stores in ChromaDB.         |
| `connect_LLM.py`   | Queries the database and generates responses using Llama 3.2. |
| `requirements.txt` | List of required dependencies.                                |
| `.gitignore`       | Prevents tracking of unnecessary files.                       |
| `scraped/`         | Stores extracted text files.                                  |

---

## **7. Notes & Troubleshooting**

### **Common Issues**

1. **Missing dependencies?**  
   Run `pip install -r requirements.txt` to install required libraries.

2. **LLM model download issues?**  
   Ensure `torch` and `transformers` are installed:

   ```bash
   pip install --upgrade torch transformers
   ```

   If the error says **"403 Client Error: Forbidden"**, it means you **haven't requested access** to Llama 3.2. Follow the **steps in section 5**.

3. **Slow query responses?**

   - Ensure ChromaDB is running efficiently.
   - Use a **GPU** for faster LLM inference.

4. **Database not found?**
   - Ensure `create_db.py` was run **before** querying the model.
   - Check if the `scraped/` directory contains text files.

---

## **8. Future Improvements**

- Enhance the **scraper** to extract structured content (tables, lists).
- Use a **larger LLM model** for better answer quality.
- Implement **Slack integration** to extract UCSC NLP Slack data (if permitted).

---

## **9. Need Help?**

If you run into issues, feel free to reach out! 🚀

---

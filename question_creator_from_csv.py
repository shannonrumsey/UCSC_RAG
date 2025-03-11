import pandas as pd
import os

# Load the CSV containing questions and categories
input_csv_path = "RAG_Questions.csv"
output_csv_path = "ucsc_questions_with_answers_3B.csv"

df = pd.read_csv(input_csv_path)

# Ensure correct column names
if "Question" not in df.columns or "Category" not in df.columns:
    raise ValueError("CSV file must contain 'Question' and 'Category' columns.")

# Create a new DataFrame for results
results = pd.DataFrame(columns=["Question", "Category", "Answer"])

# Loop through each question and retrieve answers
for index, row in df.iterrows():
    question = row["Question"]
    category = row["Category"]
    
    print(f"🔎 Asking: {question}")
    
    # Run the LLM script and capture the response
    stream = os.popen(f'python connect_LLM.py "{question}"')
    answer = stream.read().strip()
    
    print(f"✅ Answer: {answer}\n{'-'*80}")
    
    # Append result
    results = pd.concat([results, pd.DataFrame([{"Question": question, "Category": category, "Answer": answer}])], ignore_index=True)

# Save to a new CSV file
results.to_csv(output_csv_path, index=False)

print(f"\n📄 CSV file '{output_csv_path}' has been created successfully!")

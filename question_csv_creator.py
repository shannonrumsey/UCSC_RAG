import pandas as pd
import os

# Define questions with their corresponding categories
questions_with_categories = {
    "What fields can I pursue in Biomedical Science & Engineering at the UCSC grad program?": "Applying",
    "What level of degree can I get in Applied Mathematics at UCSC?": "Applying",
    "What types of art programs are offered at UCSC?": "Applying",
    "Is writing a Statement of Financial Need required?": "Applying",
    "What should I include in my statement of purpose for UCSC?": "Applying",
    "What should I include in my UCSC Personal History Statement?": "Applying",
    "Can I get a fellowship for UCSC?": "Applying",
    "Are Letters of Recommendations required for the NLP program even if I have a high GPA?": "Applying",
    "Are transcripts required for the NLP program even if I am already working in industry?": "Applying",
    "Is a résumé required for the NLP program": "Applying",
    "How long should my statement of purpose be for the NLP program": "Applying",
    "Do I need to report test scores for the Applied Economics & Finance, M.S. program?": "Applying",
    "Are test scores required for Serious Games?": "Applying",
    "What test scores do I need to report for Latin American & Latino Studies? Are they required?": "Applying",
    "Do I need test scores for Coastal Science & Policy?": "Applying",
    "Do I have to give my test scores for Music?": "Applying",
    "Do I need to report my GRE scores for the Electrical & Computer Engineering?": "Applying",
    "Can I report my GRE scores for Physics?": "Applying",
    "Are test scores needed for Ocean Sciences?": "Applying",
    "Is the History M.A. accepting applications this year?": "Applying",
    "What's the deadline for the Molecular, Cell & Developmental Biology M.S. program?": "Applying",
    "It's currently May and I haven't applied for the Natural Language Processing M.S. program yet. Did I miss my chance?": "Applying",
    "Is the deadline for the Computer Science & Engineering M.S. before or after the deadline for the Computer Science & Engineering Ph.D.?": "Applying",
    "What is the deadline for the Digital Arts and New Media M.F.A. program 2025?": "Applying",
    "When is the deadline to apply for an Education Ph.D.?": "Applying",
    "When do I need to apply for my Molecular, Cell & Developmental Biology by?": "Applying",
    "I want to apply for a Linguistics Ph.D. When is the deadline?": "Applying",
    "Are there any full tuition scholarships available for the NLP program?": "Applying",
    "How long is the NLP M.S. program?": "Applying",
    "What are my chances of finding a job in an NLP-adjacent industry after finishing my NLP M.S.?": "Applying",
    "Why should I choose NLP at UC Santa Cruz?": "Applying",
    "Who should I contact about full-tuition scholarships for NLP?": "Applying",
    "How large are the class sizes in the NLP program?": "Applying",
    "Where is the NLP campus?": "Applying",
    "What subjects are taught in the NLP program?": "Applying",
    "What health insurance is offered?": "Health Insurance",
    "Is health insurance mandatory for all UCSC students?": "Health Insurance",
    "How do I enroll in or waive the UC Student Health Insurance Plan (UC SHIP)?": "Health Insurance"
}

# Create an empty DataFrame
df = pd.DataFrame(columns=["Question", "Category", "Answer"])

# Loop through each question, run the LLM script, and capture the answer
for question, category in questions_with_categories.items():
    print(f"🔎 Asking: {question}")  # Display progress
    
    # Run the command and capture the response
    stream = os.popen(f'python connect_LLM.py "{question}"')  # Execute the LLM script
    answer = stream.read().strip()  # Read the output
    
    print(f"✅ Answer: {answer}\n{'-'*80}")  # Print answer to the terminal
    
    # Append to DataFrame using pd.concat()
    df = pd.concat([df, pd.DataFrame([{"Question": question, "Category": category, "Answer": answer}])], ignore_index=True)

# Save to CSV
csv_path = "ucsc_questions_with_answers.csv"
df.to_csv(csv_path, index=False)

print(f"\n📄 CSV file '{csv_path}' has been created successfully!")

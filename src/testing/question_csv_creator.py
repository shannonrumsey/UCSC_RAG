import pandas as pd
import os

# Define questions with their corresponding categories
questions_with_categories = {
    "What holidays are during the summer quarter?": "Registrar",
    "What classes are offerred in the NLP program?": "Registrar",
    "How many credits are the NLP courses?": "Registrar",
    "How can I change my grading option for a class?": "Registrar",
    "I want to drop a class after the deadline, what will happen?": "Registrar",
    "What should I do when one of my classes conflicts with another?": "Registrar",
    "Will I be dropped from the class if I don't go on the first day? I have a job so I won't be able to make it.": "Registrar",
    "How can I become an honors student?": "Registrar",
    "What kinds of honors are there?": "Registrar",
    "Will I lose my honors if I fail a class?": "Registrar",
    "What happens to my diploma if I change my name?": "Registrar",
    "What is a transcript?": "Registrar",
    "Where will my diploma be mailed?": "Registrar",
    "What is a CeDiploma and how is it different from a regular diploma?": "Registrar",
    "How to get UCSHIP waiver?": "Health Insurance",
    "What is the phone number for UCSHIP information?": "Health Insurance",
    "When is the add/drop deadline for master program in spring 2025?": "Registrar",
    "Can you list the final week schedule for winter 2025?": "Registrar",
    "What is the start date for the summar 2025 quarter?": "Registrar",
    "What are elective options for NLP MS program?": "Registrar",
    "If I missed tuition deadline, am I unenrolled automatically?": "Registrar",
    "What is the grading guideline for master program?": "Registrar",
    "What are the benifit of becoming an honored student?": "Registrar",
    "How do I know I am on a waitlist or not during course enrollment?": "Registrar",
    "If I lost my diploma, how do I get a new one?": "Registrar",
    "If I am a TA, does it hurt my academic standing if I receive bad evaluation from students?": "Registrar",
    "What are the additional fees beside tuition?": "Registrar",
    "What are the graduation requirements?": "Registrar",
    "Who have access to my studnet card photo?": "Registrar",
    "Is on-campus housing available at UCSC Silicon Valley campus?": "Registrar",
    "How long do I have to wait to get an official transcript once I apply?": "Registrar",
    "Can I get my tuition refund when withdraw from master program?": "Registrar"
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
csv_path = "data/outputs/ucsc_questions_with_answers.csv"
df.to_csv(csv_path, index=False)

print(f"\n📄 CSV file '{csv_path}' has been created successfully!")

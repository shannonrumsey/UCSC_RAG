import transformers
import torch
import argparse
import warnings
import sys
import re

warnings.filterwarnings('ignore')

# Set random seed for reproducibility
seed = 27
torch.manual_seed(seed)
torch.cuda.manual_seed_all(seed)
transformers.set_seed(seed)

# Select device: CUDA, MPS for Mac, or CPU
if torch.cuda.is_available():
    device = "cuda"
elif torch.backends.mps.is_available():
    device = "mps"
else:
    device = "cpu"

# Model selection (Change to a preferred instruct model if needed)
model_id = "meta-llama/Llama-3.1-8B-Instruct"

# Load the LLaMA model for direct text generation
generator = transformers.pipeline(
    "text-generation",
    model=model_id,
    torch_dtype=torch.bfloat16,
    device=device
)

# **Revised Query Function**
def query_llama(question):
    # 🔹 More controlled prompt to prevent repetition
    prompt = f"Provide a clear and concise answer to the following question.\n\nQuestion: {question}\n\nAnswer:"

    # Generate response directly from the model
    output = generator(
        prompt,
        max_new_tokens=250,  # Limit response length
        repetition_penalty=1.2,  # Reduce looping
        temperature=0.7,  # Balanced randomness
        top_k=50  # Filter unlikely words
    )

    if not output or "generated_text" not in output[0]:
        return "⚠️ Model did not return a response."

    generated = output[0]["generated_text"].strip()

    # 🔹 Ensure only the answer is extracted
    if "Answer:" in generated:
        generated = generated.split("Answer:")[-1].strip()

    # 🔹 Remove any instance of the question appearing in the response
    generated = re.sub(re.escape(question), "", generated, flags=re.IGNORECASE).strip()

    return generated

# Command-line argument parsing
parser = argparse.ArgumentParser()
parser.add_argument("question", type=str, help="The question for the model.")
args = parser.parse_args()

# Run the model
output = query_llama(args.question)

# Print only the final answer, removing question echoes
print(output)

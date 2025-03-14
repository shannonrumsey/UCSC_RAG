import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv('1B_gemini_test_results_processed.csv')

df = df[['relevance', 'accuracy', 'coherence']]


categories = {
    "Applying": list(range(1, 41)),
    "Health Insurance": list(range(41, 50)) + list(range(65, 67)) + list(range(138, 150)),
    "Registrar": list(range(50, 65)) + list(range(67, 93)),
    "NLP Wiki": list(range(93, 138))
}


def calculate_metrics(sub_df):
    return {
        "Overall Score": sub_df['accuracy'].mean(),
        "Relevance Accuracy": sub_df['relevance'].mean(),
        "Accuracy Column": sub_df['accuracy'].mean(),
        "Coherence Accuracy": sub_df['coherence'].mean(),
        "Strict Accuracy": sub_df.all(axis=1).mean()
    }


overall_metrics = calculate_metrics(df)


category_metrics = {}
for category, indices in categories.items():
    sub_df = df.iloc[np.array(indices) - 1] 
    category_metrics[category] = calculate_metrics(sub_df)


print("\n========== OVERALL METRICS ==========")
for key, value in overall_metrics.items():
    print(f"{key}: {value:.4f}")

print("\n========== CATEGORY METRICS ==========")
for category, metrics in category_metrics.items():
    print(f"\n--- {category} ---")
    for key, value in metrics.items():
        print(f"{key}: {value:.4f}")



import matplotlib.pyplot as plt
import numpy as np

colors = ['#D1E3E7', '#F9F9A6', '#FFD57F', '#A8F4A5', '#E6D0FF']
labels = list(category_metrics.keys())
x = np.arange(len(labels))
width = 0.20


fig, ax = plt.subplots(figsize=(18, 6))

bars = [
    ax.bar(x - 2*width, [category_metrics[c]["Overall Score"] for c in labels], width, label="Overall Score", color=colors[0], edgecolor="black"),
    ax.bar(x - width, [category_metrics[c]["Relevance Accuracy"] for c in labels], width, label="Average Relevance of Retrieved Data", color=colors[1], edgecolor="black"),
    ax.bar(x, [category_metrics[c]["Accuracy Column"] for c in labels], width, label="Average Accuracy of Response", color=colors[2], edgecolor="black"),
    ax.bar(x + width, [category_metrics[c]["Coherence Accuracy"] for c in labels], width, label="Average Coherence", color=colors[3], edgecolor="black"),
    ax.bar(x + 2*width, [category_metrics[c]["Strict Accuracy"] for c in labels], width, label="Strict Accuracy", color=colors[4], edgecolor="black")
]


for bar_group in bars:
    for bar in bar_group:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, height + 0.02, f'{height:.1%}', 
                ha='center', va='bottom', fontsize=12, fontweight='bold')


ax.set_ylabel("Scores", fontsize=16, fontweight='bold')
ax.set_title("Gemini 2.0 Flask Evaluation of Our RAG Model", fontsize=20, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(labels, fontsize=14, fontweight='bold')
ax.legend(fontsize=12, title_fontsize=14, prop={'weight': 'bold'})
plt.xticks(rotation=45)
plt.ylim(0, 1.1)

plt.show()


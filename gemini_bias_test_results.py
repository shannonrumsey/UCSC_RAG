import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score


df = pd.read_csv('gemini_bias_results.csv')
print(df.columns)

y_true = df['true']
y_pred = df['gemini']


accuracy = accuracy_score(y_true, y_pred)
precision = precision_score(y_true, y_pred)
recall = recall_score(y_true, y_pred)
f1 = f1_score(y_true, y_pred)
conf_matrix = confusion_matrix(y_true, y_pred)


fig, ax = plt.subplots(figsize=(5, 4))
cax = ax.matshow(conf_matrix, cmap="Blues")


for (i, j), val in np.ndenumerate(conf_matrix):
    ax.text(j, i, str(val), ha='center', va='center', color='black')


ax.set_xticks([0, 1])
ax.set_yticks([0, 1])
ax.set_xticklabels(["False", "True"])
ax.set_yticklabels(["False", "True"])
plt.xlabel("Predicted Label")
plt.ylabel("True Label")
plt.title("Confusion Matrix")


fig.colorbar(cax)


plt.savefig("confusion_matrix.png", dpi=300, bbox_inches="tight")


plt.show()


with open("gemini_eval_results.txt", "a") as f:
    f.write("\n\n\n\n")
    f.write("=============Gemini self bias evaluation results=================\n\n")
    f.write(f"Accuracy: {accuracy:.4f}\n")
    f.write(f"Precision: {precision:.4f}\n")
    f.write(f"Recall: {recall:.4f}\n")
    f.write(f"F1 Score: {f1:.4f}\n")
    f.write("Confusion Matrix:\n")
    f.write(f"{conf_matrix}\n")



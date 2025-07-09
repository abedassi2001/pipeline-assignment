import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("data/openpowerlifting.csv")

# Set seaborn style
sns.set(style="whitegrid")

# Create a figure with subplots
fig, axs = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("Distributions of Selected Columns", fontsize=16)

# 1. TotalKg Distribution
sns.histplot(df["TotalKg"], kde=True, bins=50, ax=axs[0, 0], color='skyblue')
axs[0, 0].set_title("TotalKg Distribution")
axs[0, 0].set_xlabel("TotalKg")
axs[0, 0].set_ylabel("Count")

# 2. Age Distribution
sns.histplot(df["Age"], kde=True, bins=50, ax=axs[0, 1], color='orange')
axs[0, 1].set_title("Age Distribution")
axs[0, 1].set_xlabel("Age")
axs[0, 1].set_ylabel("Count")

# 3. BodyweightKg Distribution
sns.histplot(df["BodyweightKg"], kde=True, bins=50, ax=axs[1, 0], color='green')
axs[1, 0].set_title("BodyweightKg Distribution")
axs[1, 0].set_xlabel("BodyweightKg")
axs[1, 0].set_ylabel("Count")

# 4. Sex Distribution (bar plot)
sns.countplot(x="Sex", hue="Sex", data=df, ax=axs[1, 1], palette="Set2", legend=False)
axs[1, 1].set_title("Sex Distribution")
axs[1, 1].set_xlabel("Sex")
axs[1, 1].set_ylabel("Count")

# Layout
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("data/openpowerlifting.csv")

# Show the first few rows
print("Preview of dataset:")
print(df.head())

# Basic info
print("\nDataset info:")
print(df.info())

# Plot: Histogram of BodyweightKg
plt.figure(figsize=(10, 6))
df["BodyweightKg"].dropna().hist(bins=50, color='skyblue', edgecolor='black')
plt.title("Distribution of Body Weight (Kg)")
plt.xlabel("Bodyweight (Kg)")
plt.ylabel("Frequency")
plt.grid(True)
plt.tight_layout()
plt.show()

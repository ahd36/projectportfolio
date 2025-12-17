import pandas as pd
import matplotlib.pyplot as plt

# Load CSV for balanced portfolio
df = pd.read_csv("Portfolio_Balanced_Trade-off.csv")

# Count types
type_counts = df["Type"].value_counts()

# Plot
plt.figure(figsize=(6,6))
plt.pie(type_counts, labels=type_counts.index, autopct="%1.1f%%", startangle=90)
plt.title("Figure 5:Composition of Project Types in the Balanced Portfolio", fontsize=14)

plt.savefig("Balanced_Portfolio_Composition.png", dpi=300)
plt.show()

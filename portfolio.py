# portfolio.py
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load your portfolio data (choose which one you want to visualize)
resilience_port = pd.read_csv("Portfolio_Resilience_Focused.csv")

# Step 2: Create the bar chart comparing resilience and normalized profit
plt.figure(figsize=(10,6))
plt.bar(resilience_port["Project_ID"], 
        resilience_port["Resilience_Score"], 
        label="Resilience", alpha=0.7)

plt.bar(resilience_port["Project_ID"], 
        resilience_port["NPV"] / resilience_port["NPV"].max(), 
        label="Normalized Profit", alpha=0.7)

plt.title("Project-Level Comparison: Resilience vs Profit (Resilience-Focused Portfolio)")
plt.xlabel("Project ID")
plt.ylabel("Normalized Values")
plt.legend()
plt.tight_layout()
plt.show()

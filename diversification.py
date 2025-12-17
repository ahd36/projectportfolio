import pandas as pd

# Load your dataset (assuming you have a CSV or Excel file)
df = pd.read_csv("Synthetic_Project_Portfolio.csv")
# Calculate the proportions of each project type (R&D, Strategic, Operational)
project_counts = df['Type'].value_counts()

# Calculate the proportions of each type
total_projects = len(df)
diversification_proportions = project_counts / total_projects

# Calculate Herfindahl-Hirschman Index (HHI)
HHI = (diversification_proportions**2).sum()

# Output the results
print(f"Project type proportions:\n{diversification_proportions}")
print(f"Herfindahl-Hirschman Index (HHI): {HHI}")

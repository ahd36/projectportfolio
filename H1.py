import pandas as pd

# Load your data
df = pd.read_csv("Synthetic_Project_Portfolio.csv")

# Strip spaces from column names (to avoid hidden issues)
df.columns = df.columns.str.strip()

# Count the number of projects in each type (R&D, Strategic, Operational)
project_counts = df['Type'].value_counts()

# Calculate the proportions (diversification)
total_projects = len(df)
diversification_proportions = project_counts / total_projects

# Calculate Herfindahl-Hirschman Index (HHI)
HHI = (diversification_proportions**2).sum()

# Output the proportions and HHI
print(f"Project type proportions:\n{diversification_proportions}")
print(f"Herfindahl-Hirschman Index (HHI): {HHI}")

# Add the HHI value to your dataset (the same value for all projects, as it's portfolio-wide)
df['HHI'] = HHI  # This will add the same HHI value for each project in the portfolio

# Save the modified dataframe to a new CSV if needed
df.to_csv('Disruption_Simulation_Results_with_HHI.csv', index=False)

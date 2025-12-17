import pandas as pd
import numpy as np

# Step 1: Load the grouped portfolio data
df = pd.read_csv("Portfolios_Grouped.csv")

# Step 2: Set baseline performance
df['Baseline_Performance'] = 100  # baseline score before disruption

# Step 3: Simulate disruption effects
# You can adjust the logic depending on realism

# Performance Loss (PL) based on risk level and shock sensitivity
df['Performance_Loss'] = df.apply(lambda row: row['Risk_Level'] * row['Shock_Sensitivity'] * np.random.uniform(20, 50), axis=1)

# Recovery Time (RT) based on risk level and project type
def simulate_recovery_time(row):
    base = row['Risk_Level'] * 10
    if row['Type'] == "R&D":
        return base + np.random.randint(5, 10)
    elif row['Type'] == "Strategic":
        return base + np.random.randint(8, 14)
    else:  # Operational
        return base + np.random.randint(3, 8)

df['Recovery_Time'] = df.apply(simulate_recovery_time, axis=1)

# Final Performance Level (FPL): After recovery and possible adaptation
df['Final_Performance'] = df['Baseline_Performance'] - df['Performance_Loss'] + np.random.uniform(0, 10, size=len(df))

# Step 4: Save results
df.to_csv("Disruption_Simulation_Results.csv", index=False)

# Show sample results
print(df[['Project_ID', 'Portfolio_Type', 'Performance_Loss', 'Recovery_Time', 'Final_Performance']])

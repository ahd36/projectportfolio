import pandas as pd
from scipy.stats import pearsonr

# Load the dataset with HHI
df = pd.read_csv('Disruption_Simulation_Results_with_HHI.csv')  # Make sure the path is correct
dp = pd.read_csv('Disruption_Simulation_Results.csv')
# Strip spaces from column names (if necessary)
df.columns = df.columns.str.strip()

# Calculate Performance Loss (if it's not already calculated)
# Performance Loss = 100 - Final Performance (assuming Final Performance column exists)
dp['Performance_Loss'] = 100 - dp['Final_Performance']
# Perform the correlation test between Diversification (HHI) and Performance Loss
correlation, p_value = pearsonr(df['HHI'], dp['Performance_Loss'])

# Print the correlation coefficient and p-value
print(f"Correlation coefficient: {correlation}")
print(f"P-value: {p_value}")

import pandas as pd
import matplotlib.pyplot as plt

# Assuming 'df' contains the portfolio-level data with 'Portfolio' column and 'Final_Performance' column
df = pd.read_csv('Disruption_Simulation_Results.csv')
# Group by Portfolio and calculate the mean final performance
portfolio_performance = df.groupby('Portfolio')['Final_Performance'].mean()

# Create a bar chart
plt.figure(figsize=(8,6))
portfolio_performance.plot(kind='bar', color=['skyblue', 'lightgreen', 'salmon'])
plt.title('Comparison of Final Performance Between Portfolio Types', fontsize=16)
plt.ylabel('Average Final Performance', fontsize=12)
plt.xlabel('Portfolio Type', fontsize=12)
plt.xticks(rotation=0)  # To keep the x-axis labels horizontal
plt.show()

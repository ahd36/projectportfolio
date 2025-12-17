# portfolio_composition_pies.py
import pandas as pd
import matplotlib.pyplot as plt

# Load the optimized portfolios
resilience_port = pd.read_csv("Portfolio_Resilience_Focused.csv")
profit_port = pd.read_csv("Portfolio_Profit_Focused.csv")
balanced_port = pd.read_csv("Portfolio_Balanced_Trade-off.csv")

# -----------------------------------------
# Function to plot composition by project type
# -----------------------------------------
def plot_portfolio_composition(portfolio, label):
    plt.figure(figsize=(6,6))
    portfolio["Portfolio_Type"].value_counts().plot(
        kind='pie',
        autopct='%1.1f%%',
        startangle=90,
        shadow=True,
        wedgeprops={'edgecolor': 'black'}
    )
    plt.title(f"{label} - Composition by Project Type", fontsize=13, weight='bold')
    plt.ylabel("")  # Removes default 'y' label
    plt.tight_layout()
    plt.show()

# Generate the three pie charts
plot_portfolio_composition(resilience_port, "Resilience-Focused Portfolio")
plot_portfolio_composition(profit_port, "Profit-Focused Portfolio")
plot_portfolio_composition(balanced_port, "Balanced Trade-off Portfolio")

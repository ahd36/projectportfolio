# Stage 8: Visualization & Comparative Analysis
import pandas as pd
import matplotlib.pyplot as plt

# Load the three optimized portfolios
resilience_port = pd.read_csv("Portfolio_Resilience_Focused.csv")
profit_port = pd.read_csv("Portfolio_Profit_Focused.csv")
balanced_port = pd.read_csv("Portfolio_Balanced_Trade-off.csv")

# Compute summary stats
def summarize(portfolio, label):
    total_cost = portfolio["Cost"].sum()
    total_resilience = portfolio["Resilience_Score"].sum()
    total_profit = portfolio["NPV"].sum()
    n_projects = len(portfolio)
    return {
        "Portfolio": label,
        "Total_Cost": total_cost,
        "Total_Resilience": total_resilience,
        "Total_Profit": total_profit,
        "No_Projects": n_projects
    }

summary = pd.DataFrame([
    summarize(resilience_port, "Resilience Focused"),
    summarize(profit_port, "Profit Focused"),
    summarize(balanced_port, "Balanced Trade-off")
])

print("\n📊 Portfolio Summary:")
print(summary)

# Save the summary table
summary.to_csv("Portfolio_Summary_Comparison.csv", index=False)

# ----------------------------------------------
# 📈 Step 2: Plot Resilience vs. Profit Trade-off
# ----------------------------------------------
plt.figure(figsize=(8,6))
plt.scatter(summary["Total_Profit"], summary["Total_Resilience"], s=200)

for i, txt in enumerate(summary["Portfolio"]):
    plt.annotate(txt, (summary["Total_Profit"][i]+50, summary["Total_Resilience"][i]), fontsize=10)

plt.title("Resilience vs Profit Trade-off Across Portfolios")
plt.xlabel("Total Profit (NPV)")
plt.ylabel("Total Resilience Score")
plt.grid(True)
plt.tight_layout()
plt.show()

# ----------------------------------------------
# 📊 Step 3: Portfolio Composition by Type
# ----------------------------------------------
def plot_portfolio_composition(portfolio, label):
    plt.figure(figsize=(6,6))
    portfolio["Portfolio_Type"].value_counts().plot(kind='pie', autopct='%1.1f%%')
    plt.title(f"{label} - Portfolio Composition by Type")
    plt.ylabel("")
    plt.tight_layout()
    plt.show()

plot_portfolio_composition(resilience_port, "Resilience Focused")
plot_portfolio_composition(profit_port, "Profit Focused")
plot_portfolio_composition(balanced_port, "Balanced Trade-off")

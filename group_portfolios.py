import pandas as pd

# Step 1: Load the synthetic data (must be in the same folder)
df = pd.read_csv("Synthetic_Project_Portfolio.csv")

# Step 2: Define grouping logic based on Risk_Level
def assign_portfolio(risk):
    if risk <= 0.3:
        return "Conservative"
    elif risk <= 0.6:
        return "Balanced"
    else:
        return "Aggressive"

# Step 3: Apply the function
df["Portfolio_Type"] = df["Risk_Level"].apply(assign_portfolio)

# Step 4: Save the new dataset with portfolio groups
df.to_csv("Portfolios_Grouped.csv", index=False)

# Step 5: Preview the result
print("\n📊 Portfolio Grouping Completed:\n")
print(df[["Project_ID", "Risk_Level", "Portfolio_Type"]])

print("\n✅ Grouped data saved to 'Portfolios_Grouped.csv'")

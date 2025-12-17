import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Budget_Multiplier": [8, 10, 12],
    "Total_Resilience": [6.54, 8.03, 9.10],
    "Total_Profit": [14500, 15700, 16800]
}
df = pd.DataFrame(data)

plt.figure(figsize=(8,5))
plt.plot(df["Budget_Multiplier"], df["Total_Resilience"], marker='o', label="Total Resilience")
plt.plot(df["Budget_Multiplier"], df["Total_Profit"]/df["Total_Profit"].max(), marker='o', linestyle='--', label="Normalized Profit")
plt.title("Effect of Budget on Portfolio Performance")
plt.xlabel("Budget Multiplier (× Mean Project Cost)")
plt.ylabel("Score / Normalized Profit")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

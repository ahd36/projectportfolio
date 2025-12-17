import pandas as pd

# Load the simulated disruption results
df = pd.read_csv("Disruption_Simulation_Results.csv")

# Absorptive Capacity = 100 - Performance Loss
df["Absorptive_Capacity"] = 100 - df["Performance_Loss"]

# Restorative Capacity = inverse of Recovery Time (lower time = better)
df["Restorative_Capacity"] = 1 / df["Recovery_Time"]

# Transformative Capacity = Final Performance (already simulated)
df["Transformative_Capacity"] = df["Final_Performance"]

# Optional: Normalize for scale (between 0 and 1) if needed later
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()

df[["AC_norm", "RC_norm", "TC_norm"]] = scaler.fit_transform(
    df[["Absorptive_Capacity", "Restorative_Capacity", "Transformative_Capacity"]]
)

# Save result
df.to_csv("Resilience_Dimensions.csv", index=False)

# Preview
print(df[["Project_ID", "Absorptive_Capacity", "Restorative_Capacity", "Transformative_Capacity"]].head())

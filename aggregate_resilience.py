# --------------------------------------------
# Stage 5: Resilience Score Aggregation
# --------------------------------------------
import pandas as pd

# Step 1: Load the normalized resilience data (from Stage 4)
df = pd.read_csv("Resilience_Dimensions.csv")

# Step 2: Define equal weights for ART components
w1, w2, w3 = 1/3, 1/3, 1/3  # Equal weighting

# Step 3: Compute the Resilience Score (RS)
df["Resilience_Score"] = (
    w1 * df["AC_norm"] +
    w2 * df["RC_norm"] +
    w3 * df["TC_norm"]
)

# Step 4: Save the updated dataset
df.to_csv("Resilience_Scores.csv", index=False)

# Step 5: Display sample output
print("\n✅ Resilience Scores Calculated Successfully!\n")
print(df[["Project_ID", "AC_norm", "RC_norm", "TC_norm", "Resilience_Score"]].head(10))

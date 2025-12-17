# --------------------------------------------
# Stage 6: Resilience-Based Portfolio Optimization
# --------------------------------------------
import pandas as pd
import numpy as np
import pygad

# Step 1: Load data (resilience + cost + NPV)
resilience_df = pd.read_csv("Resilience_Scores.csv")
project_df = pd.read_csv("Synthetic_Project_Portfolio.csv")

# Merge to align data
# ✅ Merge to align data properly
df = pd.merge(resilience_df, project_df, on="Project_ID", suffixes=("", "_y"))
df = df.loc[:, ~df.columns.str.endswith('_y')]  # remove duplicate columns
df.columns = df.columns.str.strip()  # clean extra spaces

print("✅ Columns in merged dataset:", df.columns.tolist())

# Step 2: Define GA parameters
num_projects = len(df)
budget_limit = df["Cost"].mean() * 12 # e.g., total allowed budget
print(f"Budget limit: {budget_limit:.2f}")

# Step 3: Define the fitness function
def fitness_function(ga_instance, solution, solution_idx):
    total_cost = np.sum(solution * df["Cost"])
    total_resilience = np.sum(solution * df["Resilience_Score"])
    
    # Apply penalty if over budget
    if total_cost > budget_limit:
        penalty = (total_cost - budget_limit) * 0.01
        total_resilience -= penalty
    
    # Ensure non-negative fitness
    return max(total_resilience, 0)



# Step 4: GA setup
gene_space = [0, 1]  # Each project can be selected (1) or not (0)

ga_instance = pygad.GA(
    num_generations=100,
    num_parents_mating=10,
    fitness_func=fitness_function,
    sol_per_pop=20,
    num_genes=num_projects,
    gene_space=gene_space,
    parent_selection_type="sss",
    keep_parents=5,
    crossover_type="single_point",
    mutation_type="random",
    mutation_percent_genes=10
)

# Step 5: Run the GA
ga_instance.run()

# Step 6: Extract the best solution
solution, solution_fitness, solution_idx = ga_instance.best_solution()
selected_projects = df[solution == 1]

# Step 7: Display results
print("\n✅ Optimal Portfolio Selected:")
print(selected_projects[["Project_ID", "NPV", "Cost", "Resilience_Score", "Type", "Portfolio_Type"]])
print(f"\n💪 Total Resilience: {solution_fitness:.4f}")
print(f"💰 Total Cost: {selected_projects['Cost'].sum():.2f}")
print(f"📊 Number of Projects: {len(selected_projects)}")

# Save selected portfolio
selected_projects.to_csv("Optimal_Resilient_Portfolio.csv", index=False)
print("\n📁 Saved as 'Optimal_Resilient_Portfolio.csv'")

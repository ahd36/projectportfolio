# Stage 7: Multi-Objective Portfolio Optimization (Resilience + Profit)
import pandas as pd
import numpy as np
import pygad

# Step 1: Load data
resilience_df = pd.read_csv("Resilience_Scores.csv")
project_df = pd.read_csv("Synthetic_Project_Portfolio.csv")

# Merge both datasets
df = pd.merge(resilience_df, project_df, on="Project_ID", suffixes=("", "_y"))
df = df.loc[:, ~df.columns.str.endswith("_y")]
df.columns = df.columns.str.strip()

# Normalize profit (NPV) for fair comparison with Resilience_Score
df["NPV_norm"] = (df["NPV"] - df["NPV"].min()) / (df["NPV"].max() - df["NPV"].min())

# Budget constraint (10× mean cost)
budget_limit = df["Cost"].mean() * 10
num_projects = len(df)

print(f"✅ Budget limit set to: {budget_limit:.2f}")
print(f"✅ Number of projects: {num_projects}")

# Step 2: Define fitness function factory for different weight settings
def make_fitness_function(weight_resilience, weight_profit):
    def fitness_function(ga_instance, solution, solution_idx):
        total_cost = np.sum(solution * df["Cost"])
        total_resilience = np.sum(solution * df["Resilience_Score"])
        total_profit = np.sum(solution * df["NPV_norm"])

        # Weighted objective
        fitness = weight_resilience * total_resilience + weight_profit * total_profit

        # Penalize over-budget portfolios
        if total_cost > budget_limit:
            fitness -= (total_cost - budget_limit) * 0.01

        return max(fitness, 0)
    return fitness_function

# Step 3: Function to run the GA
def run_optimization(weight_resilience, weight_profit, label):
    fitness_func = make_fitness_function(weight_resilience, weight_profit)

    ga_instance = pygad.GA(
    num_generations=200,
    num_parents_mating=10,
    fitness_func=fitness_func,
    sol_per_pop=50,
    num_genes=num_projects,
    gene_space=[0, 1],
    parent_selection_type="sss",
    keep_parents=5,
    crossover_type="single_point",
    mutation_type="random",
    mutation_percent_genes=10,
    random_seed=42
)


    ga_instance.run()

    best_solution, best_fitness, _ = ga_instance.best_solution()
    selected_projects = df[best_solution.astype(bool)]

    total_cost = selected_projects["Cost"].sum()
    total_resilience = selected_projects["Resilience_Score"].sum()
    total_profit = selected_projects["NPV"].sum()

    print(f"\n📊 --- {label} Portfolio ---")
    print(f"Weight (Resilience={weight_resilience}, Profit={weight_profit})")
    print(f"Total Cost: {total_cost:.2f} | Budget Limit: {budget_limit:.2f}")
    print(f"Total Resilience: {total_resilience:.4f}")
    print(f"Total Profit (NPV): {total_profit:.2f}")
    print(f"Projects Selected: {len(selected_projects)}")
    print(selected_projects[["Project_ID", "NPV", "Cost", "Resilience_Score", "Portfolio_Type"]])

    # Save to CSV
    selected_projects.to_csv(f"Portfolio_{label.replace(' ', '_')}.csv", index=False)

# Step 4: Run all three scenarios
run_optimization(1.0, 0.0, "Resilience Focused")
run_optimization(0.0, 1.0, "Profit Focused")
run_optimization(0.5, 0.5, "Balanced Trade-off")

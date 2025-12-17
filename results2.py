import matplotlib.pyplot as plt

# Example data for H5 (replace with your actual data)
performance_loss = [6.8, 10.5, 14.3, 3.5, 18.7]  # Performance loss for corresponding portfolios
recovery_time = [10, 14, 18, 8, 20]  # Recovery time in weeks

# Scatter plot for H5: Performance Loss vs. Recovery Time
plt.figure(figsize=(8, 6))
plt.scatter(performance_loss, recovery_time, color='green', label='Performance Loss vs. Recovery Time')

# Labeling the plot
plt.title('Performance Loss vs. Recovery Time (H5)', fontsize=16)
plt.xlabel('Performance Loss (%)', fontsize=12)
plt.ylabel('Recovery Time (Weeks)', fontsize=12)
plt.grid(True)
plt.legend()

# Display the plot
plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Data for the charts
categories = ['Resilience-Optimized', 'Profit-Optimized']
total_resilience = [8.20, 6.86]
final_performance = [95.2, 88.5]
performance_loss = [6.8, 18.7]

# Setting positions for bars
x = np.arange(len(categories))  # the label locations

# Bar width
width = 0.25

# Plotting the bar charts
fig, ax = plt.subplots(1, 3, figsize=(15, 5))

# Bar chart for Total Resilience
ax[0].bar(x - width, total_resilience, width, label='Total Resilience', color='skyblue')
ax[0].set_title('Total Resilience by Portfolio Strategy')
ax[0].set_ylabel('Total Resilience (out of 10)')
ax[0].set_xticks(x)
ax[0].set_xticklabels(categories)

# Bar chart for Final Performance
ax[1].bar(x, final_performance, width, label='Final Performance', color='orange')
ax[1].set_title('Final Performance by Portfolio Strategy')
ax[1].set_ylabel('Final Performance (%)')
ax[1].set_xticks(x)
ax[1].set_xticklabels(categories)

# Bar chart for Performance Loss
ax[2].bar(x + width, performance_loss, width, label='Performance Loss', color='green')
ax[2].set_title('Performance Loss by Portfolio Strategy')
ax[2].set_ylabel('Performance Loss (%)')
ax[2].set_xticks(x)
ax[2].set_xticklabels(categories)

# Add labels and legends
for ax in [ax[0], ax[1], ax[2]]:
    ax.set_xlabel('Portfolio Strategy')
    ax.legend()

# Display the chart
plt.tight_layout()
plt.show()

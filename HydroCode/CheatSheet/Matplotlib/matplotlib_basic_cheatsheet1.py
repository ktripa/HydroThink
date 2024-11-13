import matplotlib.pyplot as plt
import numpy as np

# Set up the figure
fig, axs = plt.subplots(2, 3, figsize=(10, 6), constrained_layout=True)

# 1. Line plot
x = np.linspace(0, 10, 100)
y = np.sin(x)
axs[0, 0].plot(x, y, label="Sine Wave", color='blue')
axs[0, 0].set_title("Line Plot")
axs[0, 0].legend()

# 2. Scatter plot
np.random.seed(0)
x = np.random.rand(50)
y = np.random.rand(50)
colors = np.random.rand(50)
sizes = 1000 * np.random.rand(50)
scatter = axs[0, 1].scatter(x, y, c=colors, s=sizes, alpha=0.6, cmap='viridis')
axs[0, 1].set_title("Scatter Plot")
fig.colorbar(scatter, ax=axs[0, 1], shrink=0.8)

# 3. Bar plot
categories = ['A', 'B', 'C', 'D']
values = [3, 7, 5, 9]
axs[0, 2].bar(categories, values, color=['skyblue', 'orange', 'green', 'red'])
axs[0, 2].set_title("Bar Plot")

# 4. Histogram
data = np.random.randn(1000)
axs[1, 0].hist(data, bins=20, color='purple', alpha=0.7)
axs[1, 0].set_title("Histogram")

# 5. Pie chart
sizes = [20, 30, 25, 25]
labels = ['Python', 'Matplotlib', 'Numpy', 'Pandas']
axs[1, 1].pie(sizes, labels=labels, autopct='%1.1f%%', colors=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99'])
axs[1, 1].set_title("Pie Chart")

# 6. Heatmap
data = np.random.rand(10, 10)
heatmap = axs[1, 2].imshow(data, cmap='coolwarm', aspect='auto')
fig.colorbar(heatmap, ax=axs[1, 2], shrink=0.8)
axs[1, 2].set_title("Heatmap")

# Add a main title
fig.suptitle("Matplotlib Cheat Sheet Visualization", fontsize=16)

# Save the figure
plt.savefig('matplotlib_cheatsheet_thumbnail.png', dpi=300)
plt.show()

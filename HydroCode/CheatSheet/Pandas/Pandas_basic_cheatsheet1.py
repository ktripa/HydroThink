import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create the figure
fig, axs = plt.subplots(2, 3, figsize=(10, 6), constrained_layout=True)

# 1. Create and display a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 27, 22, 32],
    'Score': [85, 90, 78, 88]
}
df = pd.DataFrame(data)
axs[0, 0].axis('tight')
axs[0, 0].axis('off')
axs[0, 0].table(cellText=df.values, colLabels=df.columns, loc='center')
axs[0, 0].set_title("DataFrame Creation")

# 2. Bar Plot for Grouped Data
grouped_data = df.groupby('Name')['Score'].sum()
axs[0, 1].bar(grouped_data.index, grouped_data.values, color='skyblue')
axs[0, 1].set_title("Grouped Bar Plot")
axs[0, 1].set_xlabel("Name")
axs[0, 1].set_ylabel("Score")

# 3. Line Plot
time_data = pd.DataFrame({
    'Date': pd.date_range(start='2023-01-01', periods=10),
    'Value': np.cumsum(np.random.randn(10))
})
axs[0, 2].plot(time_data['Date'], time_data['Value'], marker='o', linestyle='-', color='purple')
axs[0, 2].set_title("Time Series")
axs[0, 2].tick_params(axis='x', rotation=45)

# 4. Histogram
random_data = pd.DataFrame({'Values': np.random.randn(1000)})
axs[1, 0].hist(random_data['Values'], bins=20, color='orange', alpha=0.7)
axs[1, 0].set_title("Histogram of Values")

# 5. Box Plot
box_data = pd.DataFrame({
    'Group': ['A', 'A', 'B', 'B'],
    'Score': [85, 88, 78, 82]
})
axs[1, 1].boxplot(box_data['Score'], vert=True, patch_artist=True, labels=['Scores'])
axs[1, 1].set_title("Box Plot")

# 6. Scatter Plot
scatter_data = pd.DataFrame({
    'X': np.random.rand(50),
    'Y': np.random.rand(50),
    'Size': np.random.rand(50) * 1000,
    'Color': np.random.rand(50)
})
scatter = axs[1, 2].scatter(
    scatter_data['X'], scatter_data['Y'],
    s=scatter_data['Size'], c=scatter_data['Color'], cmap='viridis', alpha=0.7
)
axs[1, 2].set_title("Scatter Plot")
fig.colorbar(scatter, ax=axs[1, 2], shrink=0.8)

# Add a main title
fig.suptitle("Pandas Cheat Sheet Visualization", fontsize=16)

# Save the figure
plt.savefig('pandas_cheatsheet_thumbnail.png', dpi=300)
plt.show()

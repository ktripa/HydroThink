import numpy as np
import matplotlib.pyplot as plt

# Create the figure
fig, axs = plt.subplots(2, 3, figsize=(10, 6), constrained_layout=True)

# 1. Basic Array and Arithmetic
x = np.arange(1, 11)
y = x ** 2
axs[0, 0].plot(x, y, marker='o', label='y = x^2', color='blue')
axs[0, 0].set_title("Array Operations")
axs[0, 0].legend()

# 2. Trigonometric Functions
x = np.linspace(0, 2 * np.pi, 100)
sin_vals = np.sin(x)
cos_vals = np.cos(x)
axs[0, 1].plot(x, sin_vals, label='sin(x)', color='green')
axs[0, 1].plot(x, cos_vals, label='cos(x)', color='red')
axs[0, 1].set_title("Trigonometric Functions")
axs[0, 1].legend()

# 3. Random Numbers and Histogram
data = np.random.randn(1000)
axs[0, 2].hist(data, bins=20, color='purple', alpha=0.7)
axs[0, 2].set_title("Random Numbers")

# 4. Array Reshaping and Matrix Multiplication
A = np.arange(1, 10).reshape(3, 3)
B = np.random.randint(1, 10, (3, 3))
result = np.dot(A, B)
axs[1, 0].imshow(result, cmap='viridis', aspect='auto')
axs[1, 0].set_title("Matrix Multiplication")

# 5. Broadcasting Example
x = np.array([1, 2, 3])
y = np.array([[10], [20], [30]])
result = x + y
axs[1, 1].imshow(result, cmap='coolwarm', aspect='auto')
axs[1, 1].set_title("Broadcasting")

# 6. Fancy Indexing
x = np.linspace(-10, 10, 400)
y = np.sin(x)
mask = (x > 0) & (x < np.pi)
axs[1, 2].plot(x, y, label='sin(x)', color='orange')
axs[1, 2].scatter(x[mask], y[mask], color='red', label='Masked Points')
axs[1, 2].set_title("Fancy Indexing")
axs[1, 2].legend()

# Add a main title
fig.suptitle("NumPy Cheat Sheet Visualization", fontsize=16)

# Save the figure
plt.savefig('numpy_cheatsheet_thumbnail.png', dpi=300)
plt.show()

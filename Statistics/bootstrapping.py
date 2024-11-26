import numpy as np
import matplotlib.pyplot as plt

# Original dataset
np.random.seed(42)
data = np.random.randn(10000)  # 10000 random samples from a normal distribution

print(f"shape of data{data.shape}")
print(f"data{data}")

# Function to perform bootstrapping
def bootstrap(data, statistic, n_bootstrap=1000):
    bootstrap_samples = []
    for _ in range(n_bootstrap):
        # Sample with replacement
        sample = np.random.choice(data, size=len(data), replace=True)
        # Compute the statistic
        bootstrap_samples.append(statistic(sample))
    return np.array(bootstrap_samples)

# Bootstrap the mean
n_bootstrap = 1000
bootstrap_means = bootstrap(data, np.mean, n_bootstrap=n_bootstrap)
bootstrap_std = bootstrap(data, np.std, n_bootstrap=n_bootstrap)

# Confidence intervals
alpha = 0.05
lower_bound_mean = np.percentile(bootstrap_means, 100 * (alpha / 2))
upper_bound_mean = np.percentile(bootstrap_means, 100 * (1 - alpha / 2))

print(f"Bootstrap mean estimate: {np.mean(bootstrap_means):.2f}")
print(f"95% Confidence Interval: [{lower_bound_mean:.2f}, {upper_bound_mean:.2f}]")

# Plotting bootstrapped mean
plt.hist(bootstrap_means, bins=30, alpha=0.7, color='blue', edgecolor='k', density=True)
plt.axvline(lower_bound_mean, color='red', linestyle='--', label='Lower CI Bound')
plt.axvline(upper_bound_mean, color='red', linestyle='--', label='Upper CI Bound')
plt.axvline(np.mean(data), color='green', linestyle='-', label='Original Mean')
plt.title('Bootstrap Distribution of the Mean')
plt.xlabel('Mean')
plt.ylabel('Density')
plt.legend()
plt.savefig('Statistics/Plots/bootstrapping.png',dpi=300)
plt.show()
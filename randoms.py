import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# Generate Random Number
x = random.randint(100)
print(x)
print()

# Generate Random Float
x = random.rand()
print(x)
print()

# Generate Random Array
x = random.randint(100, size=(5))
print(x)
print()

# Generate Random 2-D Array
x = random.randint(100, size=(3, 5))
print(x)
print()

# Generate Random 3-D Array
x = random.randint(100, size=(3, 5, 2))
print(x)
print()

# Generate random number from array
x = random.choice([3, 5, 7, 9])
print(x)
print()

# Generate a 2-D array that consists of the values in the array parameter (3, 5, 7, and 9)
x = random.choice([3, 5, 7, 9], size=(3, 5))
print(x)
print()

# Generate a 1-D array containing 100 values, where each value has to be 3, 5, 7 or 9.
# The probability for the value to be 3 is set to be 0.1
# The probability for the value to be 5 is set to be 0.3
# The probability for the value to be 7 is set to be 0.6
# The probability for the value to be 9 is set to be 0
x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0], size=(100))
print(x)
print()

# Same example as above, but return a 2-D array with 3 rows, each containing 5 values
x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0], size=(3, 5))
print(x)
print()

# Shuffle an array
arr = np.array([1, 2, 3, 4, 5])
random.shuffle(arr)
print(arr)
print()

# Generate a random permutation of elements of an array
arr = np.array([1, 2, 3, 4, 5])
print(random.permutation(arr))
print()

# Plotting a Distplot
sns.distplot([0, 1, 2, 3, 4, 5])
plt.show()

# Plotting a Distplot Without the Histogram
sns.distplot([0, 1, 2, 3, 4, 5], hist=False)
plt.show()

# Generating a Random Normal Distribution of size 2x3
x = random.normal(size=(2, 3))
print(x)
print()

# Generating a Random Normal Distribution of size 2x3 with mean at 1 and standard deviation of 2
x = random.normal(loc=1, scale=2, size=(2, 3))
print(x)
print()

# Visualizing a Normal Distribution
sns.distplot(random.normal(size=1000), hist=False)
plt.show()

# Binomial Distribution
x = random.binomial(n=10, p=0.5, size=10)
print(x)
print()

# Visualizing a Binomial Distribution
sns.distplot(random.binomial(n=10, p=0.5, size=1000), hist=True, kde=False)
plt.show()

# Poisson Distribution
x = random.poisson(lam=2, size=10)
print(x)
print()

# Visualizing a Poisson Distribution
sns.distplot(random.poisson(lam=2, size=1000), kde=False)
plt.show()

# Uniform Distribution
x = random.uniform(size=(2, 3))
print(x)
print()

# Visualizing a Uniform Distribution
sns.distplot(random.uniform(size=1000), hist=False)
plt.show()

# Logistic Distribution
x = random.logistic(loc=1, scale=2, size=(2, 3))
print(x)
print()

# Visualizing a Logistic Distribution
sns.distplot(random.logistic(size=1000), hist=False)
plt.show()

# Multinomial Distribution
x = random.multinomial(n=6, pvals=[1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6])
print(x)
print()

# Visualizing a Multinomial Distribution
x = random.multinomial(
    n=6, pvals=[1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6], size=1000)
sns.distplot(x, hist=True, kde=False)
plt.show()

# Exponential Distribution
x = random.exponential(scale=2, size=(2, 3))
print(x)
print()

# Visualizing an Exponential Distribution
sns.distplot(random.exponential(size=1000), hist=False)
plt.show()

# Chi Square Distribution
x = random.chisquare(df=2, size=(2, 3))
print(x)
print()

# Visualizing a Chi Square Distribution
sns.distplot(random.chisquare(df=1, size=1000), hist=False)
plt.show()

# Rayleigh Distribution
x = random.rayleigh(scale=2, size=(2, 3))
print(x)
print()

# Visualizing a Rayleigh Distribution
sns.distplot(random.rayleigh(size=1000), hist=False)
plt.show()

# Pareto Distribution
x = random.pareto(a=2, size=(2, 3))
print(x)
print()

# Visualizing a Pareto Distribution
sns.distplot(random.pareto(a=2, size=1000), kde=False)
plt.show()

# Zipf Distribution
x = random.zipf(a=2, size=(2, 3))
print(x)
print()

# Visualizing a Zipf Distribution
x = random.zipf(a=2, size=1000)
sns.distplot(x[x < 10], kde=False)
plt.show()

import numpy as np
import math
import matplotlib.pyplot as plt
import scipy.stats as stats

# prior
a = 0
b_squared = 1

# posterior
x = 0
y_squared = 0

samples = []
with open('q3_sigma3.dat', 'r') as f:
    lines = f.readlines()
    for line in lines:
        sample = line.split(", ")
        sample = list(map(lambda x:float(x), sample)) # map each data point from string to float
        samples.append(sample)
# print(samples)

print("Table for sigma 3")
for sample in samples:
    n = len(sample)
    sample = np.array(sample)
    avg = sample.mean()
    var = 9 / n
    standard_error_squared = var / n
    x = (b_squared * avg + standard_error_squared * a) / (b_squared+standard_error_squared)
    y_squared = (b_squared*standard_error_squared) / (b_squared+standard_error_squared)
    print(str(x) + "   " +str(y_squared))

    # plot the posterior distribution
    sigma = math.sqrt(y_squared)
    numbers = np.linspace(4, 6, 100)
    plt.plot(numbers, stats.norm.pdf(numbers, x, sigma))
    plt.show()

    # update a and b^2
    a = x
    b_squared = y_squared

#========================================================================================================================
# (b)

# prior
a = 0
b_squared = 1

# posterior
x = 0
y_squared = 0

samples = []
with open('q3_sigma100.dat', 'r') as f:
    lines = f.readlines()
    for line in lines:
        sample = line.split(", ")
        sample = list(map(lambda x:float(x), sample)) # map each data point from string to float
        samples.append(sample)
# print(samples)

print("Table for sigma 100")
for sample in samples:
    n = len(sample)
    sample = np.array(sample)
    avg = sample.mean()
    var = 10000 / n
    standard_error_squared = var / n
    x = (b_squared * avg + standard_error_squared * a) / (b_squared+standard_error_squared)
    y_squared = (b_squared*standard_error_squared) / (b_squared+standard_error_squared)
    print(str(x) + "   " +str(y_squared))

    # plot the posterior distribution
    sigma = math.sqrt(y_squared)
    numbers = np.linspace(-5, 5, 100)
    plt.plot(numbers, stats.norm.pdf(numbers, x, sigma))
    plt.show()

    # update a and b^2
    a = x
    b_squared = y_squared



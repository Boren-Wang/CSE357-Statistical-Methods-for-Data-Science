import numpy as np

def square(n):
    return n**2

def prob(sample):
    counter = 0
    for i in sample:
        if i > 10:
            counter += 1
    print(counter / len(sample))

s1 = np.random.normal(0, 1, 100)
s1 = list(map(square, s1))

s2 = np.random.normal(0, 1, 10000)
s2 = list(map(square, s2))

s3 = np.random.normal(0, 1, 1000000)
s3 = list(map(square, s3))

prob(s1)
prob(s2)
prob(s3)

# n=10^2 -> P(Q>10) = 0.0
# n=10^4 -> P(Q>10) = 0.002
# n=10^6 -> P(Q>10) = 0.001531

# a = 1/10 = 0.1
# b = 4/81 = 0.04938
# In all three cases, P(Q>10) < 0.04938 and P(Q>10) < 0.1

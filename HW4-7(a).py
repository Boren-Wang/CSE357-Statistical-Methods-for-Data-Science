import numpy as np
import math
X_sample = []
Y_sample = []
with open('q7_X.dat', 'r') as f:
    d = f.readlines()
    for i in d:
        X_sample.append(float(i))

with open('q7_Y.dat', 'r') as f:
    d = f.readlines()
    for i in d:
        Y_sample.append(float(i))

n = len(X_sample)
m = len(Y_sample)
X_sample = np.array(X_sample)
Y_sample = np.array(Y_sample)

# print(X_sample)
# print(Y_sample)

average_X = X_sample.mean()
print("Average of the sample X is "+str(average_X))
average_Y = Y_sample.mean()
print("Average of the sample Y is "+str(average_Y))
difference = average_X - average_Y
print("Difference is "+str(difference))

variance_X = X_sample.var()
variance_Y = X_sample.var()
print("Variance of the sample X is "+str(variance_X))
print("Variance of the sample Y is "+str(variance_Y))

se_estimate = math.sqrt(variance_X/n + variance_Y/m)
print("The estimate for the standard error is "+str(se_estimate))

W = abs(difference / se_estimate)
Z = 1.96 # Z_0.025

print("W is "+str(W))
print("W is greater than 1.96 => Reject the null hypothesis => the population means of X and Y are not the same")

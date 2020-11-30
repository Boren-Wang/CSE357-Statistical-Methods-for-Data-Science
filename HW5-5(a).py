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

X_sample = np.array(X_sample)
Y_sample = np.array(Y_sample)


average_X = X_sample.mean()
print("Average of the sample X is "+str(average_X))
average_Y = Y_sample.mean()
print("Average of the sample Y is "+str(average_Y))
average_difference = average_X - average_Y
print("Average of D is "+str(average_difference))

sum = 0
for i in range(n):
    Di = X_sample[i]-Y_sample[i]
    sum += (Di-average_difference)**2
sample_variance = sum / (n-1)
sample_std = math.sqrt(sample_variance)
print("sample standard deviation is "+str(sample_std))

denominator = sample_std / math.sqrt(n)
T = average_difference / denominator
print("T is "+str(T))
T_abs = abs(T)
print("T absolute is "+str(T_abs))
print("|T| is greater than the threshold 1.962 => Reject the null hypothesis => the population means of X and Y are not the same")
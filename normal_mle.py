from math import sqrt
sample = []

with open('acceleration_normal.csv', 'r', encoding="utf-8-sig") as f:
    d = f.readlines()
    for i in d:
        sample.append(float(i))

n = len(sample)

sum = 0
for i in sample:
    sum += i

u_mle = round(sum / n, 3)

nominator = 0
for i in sample:
    nominator += (i-u_mle)**2
o_mle = round(sqrt(nominator/n), 3)

print("u_MLE is "+str(u_mle))
print("o_MLE is "+str(o_mle))


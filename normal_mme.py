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

u_mme = round(sum / n, 3)

nominator = 0
for i in sample:
    nominator += (i-u_mme)**2
o_mme = round(sqrt(nominator/n), 3)

print("u_MME is "+str(u_mme))
print("o_MME is "+str(o_mme))
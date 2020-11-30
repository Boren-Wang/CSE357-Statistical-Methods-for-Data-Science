from math import sqrt
sample = []

with open('model_uniform.csv', 'r', encoding="utf-8-sig") as f:
    d = f.readlines()
    for i in d:
        sample.append(float(i))

n = len(sample)

sum = 0
for i in sample:
    sum += i

average = sum / n
nominator = 0
for i in sample:
    nominator += (i-average)**2
std = sqrt(nominator/n)

a_mme = round(average - sqrt(3)*std, 3)
b_mme = round(average + sqrt(3)*std, 3)

print("a_MME is "+str(a_mme))
print("b_MME is "+str(b_mme))


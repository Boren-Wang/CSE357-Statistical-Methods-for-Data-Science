sample = []

with open('mpg_exponential.csv', 'r', encoding="utf-8-sig") as f:
    d = f.readlines()
    for i in d:
        sample.append(float(i))

n = len(sample)

sum = 0
for i in sample:
    sum += i

lambda_mle = round(n / sum, 3) # n / sum of Xi

print("MLE for the lambda of mpg_exponential.csv is "+str(lambda_mle))
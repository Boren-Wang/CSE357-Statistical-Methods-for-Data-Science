sample = []

with open('model_uniform.csv', 'r', encoding="utf-8-sig") as f:
    d = f.readlines()
    for i in d:
        sample.append(float(i))

n = len(sample)

a_mle = round(min(sample), 3)
b_mle = round(max(sample), 3)
print("a_MLE is "+str(a_mle))
print("b_MLE is "+str(b_mle))

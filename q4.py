import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

data_1999 = []
data_2009 = []
data_2019 = []

with open('1999.csv', 'r', encoding="utf-8-sig") as f:
    d = f.readlines()
    for i in d:
        data_1999.append(float(i))

with open('2009.csv', 'r', encoding="utf-8-sig") as f:
    d = f.readlines()
    for i in d:
        data_2009.append(float(i))

with open('2019.csv', 'r', encoding="utf-8-sig") as f:
    d = f.readlines()
    for i in d:
        data_2019.append(float(i))


len_1999 = len(data_1999)
len_2009 = len(data_2009)
len_2019 = len(data_2019)

print("==========")
print("(a)")
# (a) 1999 vs. 2009
T_obs = abs(np.mean(data_1999)-np.mean(data_2009))
p_value = 0
for i in range(200):
    # combine
    data = data_1999 + data_2009
    # permute
    permuted = np.random.permutation(data).tolist()
    # split
    new_1999 = permuted[0:len_1999]
    new_2009 = permuted[len_1999:len(data)]
    # difference
    T_i = abs(np.mean(new_1999)-np.mean(new_2009))
    # print(T_i)
    # p-value
    if T_i>T_obs:
        p_value+=1
p_value = p_value / 200
print("1999 vs. 2009")
print("p value for 1999 vs. 2009 with n=200 is "+str(p_value))
print("p value < 0.05 => reject the null hypothesis")

# (a) 2009 vs. 2019
T_obs = abs(np.mean(data_2019)-np.mean(data_2009))
p_value = 0
for i in range(200):
    # combine
    data = data_2019 + data_2009
    # permute
    permuted = np.random.permutation(data).tolist()
    # split
    new_2019 = permuted[0:len_2019]
    new_2009 = permuted[len_2019:len(data)]
    # difference
    T_i = abs(np.mean(new_2019)-np.mean(new_2009))
    # print(T_i)
    # p-value
    if T_i>T_obs:
        p_value+=1
p_value = p_value / 200
print("2009 vs. 2019")
print("p value for 2009 vs. 2019 with n=200 is "+str(p_value))
print("p value < 0.05 => reject the null hypothesis")

print("==========")
print("(b)")
# (b) 1999 vs. 2009
T_obs = abs(np.mean(data_1999)-np.mean(data_2009))
p_value = 0
for i in range(2000):
    # combine
    data = data_1999 + data_2009
    # permute
    permuted = np.random.permutation(data).tolist()
    # split
    new_1999 = permuted[0:len_1999]
    new_2009 = permuted[len_1999:len(data)]
    # difference
    T_i = abs(np.mean(new_1999)-np.mean(new_2009))
    # print(T_i)
    # p-value
    if T_i>T_obs:
        p_value+=1
p_value = p_value / 200
print("1999 vs. 2009")
print("p value for 1999 vs. 2009 with n=2000 is "+str(p_value))
print("p value < 0.05 => reject the null hypothesis")

# (b) 2009 vs. 2019
T_obs = abs(np.mean(data_2019)-np.mean(data_2009))
p_value = 0
for i in range(2000):
    # combine
    data = data_2019 + data_2009
    # permute
    permuted = np.random.permutation(data).tolist()
    # split
    new_2019 = permuted[0:len_2019]
    new_2009 = permuted[len_2019:len(data)]
    # difference
    T_i = abs(np.mean(new_2019)-np.mean(new_2009))
    # print(T_i)
    # p-value
    if T_i>T_obs:
        p_value+=1
p_value = p_value / 200
print("2009 vs. 2019")
print("p value for 2009 vs. 2019 with n=2000 is "+str(p_value))
print("p value < 0.05 => reject the null hypothesis")

print("==========")
print("(c)")
# !!!These are the helper functions I wrote for my HW3-3!!!
def plot_eCDF(sample1, sample2, year1, year2):
    sorted_sample = sorted(sample1)
    length = len(sample1)

    X = remove_duplicates(sorted_sample)
    Y = []
    y = 0

    for x in X:
        count = sample1.count(x)
        y = y + count / length
        Y.append(y)

    X, Y = process_for_step_ladder_shape(X, Y)

    plt.figure('KS Test')
    plt.plot(X, Y, label=year1)

    # ==========
    sorted_sample = sorted(sample2)
    length = len(sample2)

    X = remove_duplicates(sorted_sample)
    Y = []
    y = 0

    for x in X:
        count = sample2.count(x)
        y = y + count / length
        Y.append(y)

    X, Y = process_for_step_ladder_shape(X, Y)
    plt.figure('KS Test')
    plt.plot(X, Y, label=year2)

    plt.xlabel('x')
    plt.ylabel('Pr[X<=x]')
    plt.legend(loc="upper left")
    plt.grid()
    plt.show()

    result = stats.ks_2samp(sample1, sample2)
    # max_difference = result[0]
    print(year1+" vs. "+year2)
    print("Max difference between the two eCDFs is " + str(result[0]))
    if result[0] > 0.05:
        print("Max difference > 0.05 => reject the null hypothesis")
    else:
        print("Max difference <= 0.05 => accept the null hypothesis")

def remove_duplicates(arr):
    res = []
    for i in arr:
        if i not in res:
            res.append(i)
    return res

def process_for_step_ladder_shape(X, Y): # process X and Y so that the eCDF graph will be in a step-ladder shape
    delta = .1
    new_X = [min(X)-delta]
    new_Y = [0]

    for i in range(len(X)):
        new_X = new_X + [X[i], X[i]]

        if i == 0:
            new_Y = new_Y + [0, Y[i]]
        else:
            new_Y = new_Y + [Y[i-1], Y[i]]
    new_X = new_X + [max(X) + delta]
    new_Y = new_Y + [1]
    return new_X, new_Y

# (c) 1999 vs. 2009
plot_eCDF(data_1999, data_2009, "1999", "2009")


# (c) 2009 vs. 2019
plot_eCDF(data_2009, data_2019, "2009", "2019")



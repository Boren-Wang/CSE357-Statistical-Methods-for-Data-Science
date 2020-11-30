sample = [0.13, 2.91, 1.2, 1.2] # sample for part(a)

s1 = [1, 3, 5, 6]
s2 = [2, 3, 4, 6]
samples = [s1, s2] # a collection of list of samples for part(c)





# Part(a) Part(a) Part(a) Part(a) Part(a)
import matplotlib.pyplot as plt
import random

def plot_eCDF(sample):
    sorted_sample = sorted(sample)
    length = len(sample)

    X = remove_duplicates(sorted_sample)
    Y = []
    y = 0

    for x in X:
        count = sample.count(x)
        y = y + count / length
        Y.append(y)
    # print(X)
    # print(Y)

    X, Y = process_for_step_ladder_shape(X, Y)
    # print(X)
    # print(Y)

    plt.figure('eCDF')
    plt.plot(X, Y, label='eCDF')
    plt.scatter(sorted_sample, [0] * length, color='red', marker='x', s=50, label='samples')
    plt.xlabel('x')
    plt.ylabel('Pr[X<=x]')
    plt.title('eCDF with %d samples.' % length)
    plt.legend(loc="upper left")
    plt.grid()
    plt.show()

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

plot_eCDF(sample) # Comment this line if you do not want part(a) to be executed





# Part(b) Part(b) Part(b) Part(b) Part(b)
def generate_random_samples(size):
    res = []
    for i in range(size):
        n = random.randint(1, 99) # 1-99
        res.append(n)
    return res

sample_10 = generate_random_samples(10)
sample_100 = generate_random_samples(100)
sample_1000 = generate_random_samples(1000)

plot_eCDF(sample_10) # Comment this line if you do not want part(b) to be executed
plot_eCDF(sample_100) # Comment this line if you do not want part(b) to be executed
plot_eCDF(sample_1000) # Comment this line if you do not want part(b) to be executed






# Part(c) Part(c) Part(c) Part(c) Part(c)
def plot_average_eCDF(samples):
    X = []
    Y = []
    input_points = [] # used to show all samples on the x-axis
    list_of_dictionaries = []
    for sample in samples:
        y = 0
        dictionary = {} # eCDF for sample from 1 to 99
        length = len(sample)
        for i in range(1, 100):
            y = y + sample.count(i) / length
            dictionary[i] = y
        input_points += sample
        list_of_dictionaries.append(dictionary)

    X = sorted(remove_duplicates(input_points))
    for x in X:
        total_eCDF = 0
        number_of_students = len(samples)
        for dictionary in list_of_dictionaries:
            if x in dictionary:
                total_eCDF += dictionary[x]
        average_eCDF = total_eCDF / number_of_students
        Y.append(average_eCDF)

    X, Y = process_for_step_ladder_shape(X, Y)
    # print(X)
    # print(Y)

    plt.figure('Average eCDF')
    plt.plot(X, Y, label='Average eCDF')
    plt.scatter(input_points, [0] * len(input_points), color='red', marker='x', s=50, label='samples')
    plt.xlabel('x')
    plt.ylabel('Pr[X<=x]')
    plt.title("Average eCDF with "+str(len(input_points))+" samples in total from "+str(len(samples))+" students.")
    plt.legend(loc="upper left")
    plt.grid()
    plt.show()

plot_average_eCDF(samples) # Comment this line if you do not want part(c) to be executed





# Part(d) Part(d) Part(d) Part(d) Part(d)
def generate_10_samples_for_n_students(n):
    res = []
    for i in range(n):
        res.append(generate_random_samples(10))
    return res

plot_average_eCDF(generate_10_samples_for_n_students(10)) # Comment this line if you do not want part(d) to be executed
plot_average_eCDF(generate_10_samples_for_n_students(100)) # Comment this line if you do not want part(d) to be executed
plot_average_eCDF(generate_10_samples_for_n_students(1000)) # Comment this line if you do not want part(d) to be executed






# Part(e) Part(e) Part(e) Part(e) Part(e)
import math
import numpy as np

def plot_eCDF_with_confidence_intervals(sample):
    sorted_sample = sorted(sample)
    length = len(sample)

    X = remove_duplicates(sorted_sample)
    Y = []
    y = 0

    for x in X:
        count = sample.count(x)
        y = y + count / length
        Y.append(y)
    # print(X)
    # print(Y)

    z = 1.96
    standard_error = math.sqrt(np.var(Y)/length)
    upper = [] # upper bounds of the CIs
    lower = [] # lower bounds of the CIs
    for i in range(len(Y)):
        y = Y[i]
        up = y+z*standard_error
        low = y-z*standard_error
        upper.append(up)
        lower.append(low)
    # print(upper)
    # print(lower)

    new_X, new_Y = process_for_step_ladder_shape(X, Y)


    upper = process_for_step_ladder_shape(X, upper)[1]
    lower = process_for_step_ladder_shape(X, lower)[1]

    X_for_confidence_intervals = new_X[2:len(new_X) - 1]
    upper = upper[2:len(upper)-1]
    lower = lower[2:len(lower)-1]

    plt.figure('eCDF')
    plt.plot(new_X, new_Y, label='eCDF')
    plt.plot(X_for_confidence_intervals, upper, label='upper bounds')
    plt.plot(X_for_confidence_intervals, lower, label='lower bounds')
    plt.scatter(sorted_sample, [0] * length, color='red', marker='x', s=50, label='samples')
    plt.xlabel('x')
    plt.ylabel('Pr[X<=x]')
    plt.title('eCDF with 95% normal based CIs for collisions.csv.')
    plt.legend(loc="upper left")
    plt.grid()
    plt.show()

collisions = np.genfromtxt('collisions.csv', delimiter=',').tolist()
collisions[0] = 393

plot_eCDF_with_confidence_intervals(collisions) # Comment this line if you do not want part(e) to be executed



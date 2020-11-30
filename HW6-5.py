n = 576//4
# print(n)
parts = []
with open('q5.dat', 'r') as f:
    lines = f.readlines()
    x = []
    sample = []
    for line in lines:
        if n>0:
            x.append(int(line.split()[0]))
            value = line.split()[1]
            sample.append(int(value))
            n-=1
        else:
            parts.append((x, sample))
            x = []
            sample = []
            x.append(int(line.split()[0]))
            value = line.split()[1]
            sample.append(int(value))
            n = (576//4) - 1
    parts.append((x, sample))

from sklearn import linear_model
import matplotlib.pyplot as plt
import numpy as np

for i in range(4):
    train_x = np.array(parts[i][0]).reshape(-1, 1)
    train_y = np.array(parts[i][1]).reshape(-1, 1)
    regressor = linear_model.LinearRegression()
    regressor.fit(train_x, train_y)
    predict_y = regressor.predict(train_x)

    plt.scatter(train_x, train_y)
    plt.plot(train_x, predict_y, color='red')
    plt.show()

    SSE = 0
    # calculate the SSE
    for j in range(len(train_y)):
        # print(predict_y[i][0])
        # print(train_y[i][0])
        dif = predict_y[i][0] - train_y[i][0]
        # print(dif)
        # print("-----")
        SSE += dif**2
    print("SSE for part " + str(i+1) + ": " +str(SSE))
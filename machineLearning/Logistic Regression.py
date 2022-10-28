import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

data = pd.read_csv('data_classification.csv',header=None)


tmpX0 = []
tmpX1 = []
tmpY = []
i=0
tmp_test_X0 = []
tmp_test_X1 = []


for item in data.values:
    if i > 80:
        tmp_test_X0.append(item[0])
        tmp_test_X1.append(item[1])
    tmpX0.append(item[0])
    tmpX1.append(item[1])
    tmpY.append(item[2])
    i += 1


X_train = np.array([tmpX0,tmpX1])
Y_train = np.array([tmpY])
X_test = np.array([tmp_test_X0,tmp_test_X1])





#plt.show()

def sigmoid(z):
    return 1/(1+np.exp(-z))

def boudary(hypothesis):
    if hypothesis >= 0.5:
        return 1
    if hypothesis < 0.5:
        return 0

def predict(features, weight):
    return sigmoid(np.dot(weight.T, features))

def cost_function(featuers, labels, weight):
    n = len(labels)
    predictation = predict(featuers, labels)
    costFunction = -1/n*(np.dot(labels.T, np.exp(predictation))+ ( (1-labels).T*np.exp(1-predictation)))
    return costFunction.sum()

def logistic_regression(features, labels, learning_rate, start):
    w = [start]

    for i in range(400):


        z_i = sigmoid(np.dot(features.T,w[-1]))

        w_new = w[-1] - learning_rate*(np.dot(features, (z_i-labels.T)))
        if np.linalg.norm(np.dot(features, (z_i-labels.T))) / len(w_new) < 1e-3 :
            break

        w.append(w_new)
    return w


# extended data

train_X = np.concatenate((np.ones((1, X_train.shape[1])), X_train), axis = 0)

d = train_X.shape[0]
w_init = np.random.randn(d, 1)

w = logistic_regression(train_X, Y_train, 0.001, w_init )

X_test = np.concatenate((np.ones((1, X_test.shape[1])), X_test), axis = 0)
print(X_test.shape)
print(w[-1].shape)
print(w[-1])
pre = predict(w[-1],X_test)
print(X_test)
ket_qua = []
for i in pre:
    ket_qua.append(boudary(i))
print(ket_qua)



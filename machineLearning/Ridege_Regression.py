import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge
def sample_data(num_points):
    x = np.random.rand(num_points) - 0.5
    y = np.sin(2 * np.pi * (x+0.5)) + 0.1*np.random.randn(num_points)
    return x,y

np.random.seed(1) # to make the results reproducible despite (pseudo)-randomness

train_data = sample_data(20)
test_data = sample_data(200)

xs_plot = np.arange(-0.5, 0.5, 0.01)
ys_plot = np.sin(2 * np.pi * (xs_plot+0.5))

X_train = train_data[0].reshape((-1,1))
y_train = train_data[1]
y_train_sine = train_data[1]
X_test = test_data[0].reshape((-1,1))
y_test = test_data[1]
y_test_sine = test_data[1]

lin_reg = LinearRegression() # "untrained model"
lin_reg.fit(X_train, y_train)

poly = PolynomialFeatures(degree=10, include_bias=False)
x_features = poly.fit_transform(X_train)
x_features_test = poly.fit_transform(X_test)
lin_reg1 = LinearRegression()
lin_reg1.fit(x_features, y_train)
predictions = lin_reg1.predict(np.hstack([xs_plot.reshape(-1, 1)**k for k in range(1, 11)])).reshape(np.size(xs_plot),)

scaler = StandardScaler()
scaler.fit(x_features) # initialize the parameters `mean_` and `scale_` based on the TRAINING data
scaler_sine = scaler # a copy for later use
train_normalized_new = scaler.transform(x_features) # scale the training data (polynomial features)
test_normalized_new = scaler.transform(x_features_test) # scale the test data (polynomial features)

rig_reg = Ridge(alpha=1)
rig_reg.fit(train_normalized_new, y_train)
x_scale = scaler.transform(np.hstack([xs_plot.reshape((-1, 1))**k for k in range(1,11)]))
predictions1 = rig_reg.predict(x_scale)

plt.subplot(1, 2, 1)
plt.plot(xs_plot, predictions, color='blue', label="Feature Engineering")
plt.scatter(train_data[0], train_data[1], color='red', label="train data")
plt.scatter(test_data[0], test_data[1], color='green', label="test data", alpha=0.5)
plt.legend()

plt.subplot(1,2, 2)
plt.plot(xs_plot, predictions1, label="Ridge Regression")
plt.scatter(train_data[0], train_data[1], color='red', label="train data")
plt.scatter(test_data[0], test_data[1], color='green', label="test data", alpha=0.5)
plt.legend()
plt.savefig("Image.pdf")
plt.show()


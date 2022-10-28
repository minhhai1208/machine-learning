
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist
from mnist.loader import MNIST

def kmeans_display(X, label):
    K = np.amax(label) + 1
    X0 = X[label == 0, :]
    X1 = X[label == 1, :]
    X2 = X[label == 2, :]

    plt.plot(X0[:, 0], X0[:, 1], 'b^', markersize=4, alpha=.8)
    plt.plot(X1[:, 0], X1[:, 1], 'go', markersize=4, alpha=.8)
    plt.plot(X2[:, 0], X2[:, 1], 'rs', markersize=4, alpha=.8)

    plt.axis('equal')
    plt.plot()
    plt.show()


def kmeans_init_centers(X, k):
    # randomly pick k rows of X as initial centers

    print(X[np.random.choice(X.shape[0], k, replace=False)])
    return X[np.random.choice(X.shape[0], k, replace=False)]

def kmeans_assign_labels(X, centers):
    # calculate pairwise distances btw data and centers
    D = cdist(X, centers)
    print("Argmin",np.argmin(D, axis = 1))
    print((np.argmin(D, axis = 1)).shape)
    # return index of the closest center
    return np.argmin(D, axis = 1)

def kmeans_assign_labels1(X, centers):
    # calculate pairwise distances btw data and centers

    x = np.array([1,2])
    eta = 0.5
    return myGD(x, eta)


def grad(X,centers):
    return cdist(X,centers)

def kmeans_update_centers(X, labels, K):
    centers = np.zeros((K, X.shape[1]))
    for k in range(K):
        # collect all points assigned to the k-th cluster
        Xk = X[labels == k]
        print("Lan k:",k)
        print("Xk:",Xk)
        # take average
        centers[k,:] = np.mean(Xk, axis = 0)
        print(centers[k])

    return centers

def myGD(w_init, eta):
    w = [w_init]
    for it in range(100):
        w_new = w - eta*grad(w)
        if np.linalg.norm(grad(w_new))/len(w_new) < 1e-3:
            break
        w.append(w_new)
    return w

def has_converged(centers, new_centers):
    # return True if two sets of centers are the same
    return (set([tuple(a) for a in centers]) ==
        set([tuple(a) for a in new_centers]))

def kmeans(X, K):
    centers = [kmeans_init_centers(X, K)]
    print("Centers",centers)
    labels = []
    it = 0
    while True:
        labels.append(kmeans_assign_labels(X, centers[-1]))
        new_centers = kmeans_update_centers(X, labels[-1], K)
        if has_converged(centers[-1], new_centers):
            break
        centers.append(new_centers)
        it += 1
    return (centers, labels, it)

def kmeans1(X, K):
    centers = [kmeans_init_centers(X, K)]
    print("Centers",centers)
    labels = []
    it = 0
    while True:
        labels.append(kmeans_assign_labels1(X, centers[-1]))
        new_centers = kmeans_update_centers(X, labels[-1], K)
        if has_converged(centers[-1], new_centers):
            break
        centers.append(new_centers)
        it += 1
    return (centers, labels, it)


means = [[2, 2], [8, 3], [3, 6]]
cov = [[1, 0], [0, 1]]
N = 500
X0 = np.random.multivariate_normal(means[0], cov, N)
X1 = np.random.multivariate_normal(means[1], cov, N)
X2 = np.random.multivariate_normal(means[2], cov, N)

X = np.concatenate((X0, X1, X2), axis = 0)
K = 3

original_label = np.asarray([0]*N + [1]*N + [2]*N).T

kmeans_display(X, original_label)

(centers, labels, it) = kmeans(X, K)
print('Centers found by our algorithm:')
print(centers[0])
print(centers)

print("Label",labels)
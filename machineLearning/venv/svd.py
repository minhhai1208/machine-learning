import numpy as np
from numpy import linalg as la


def svd_rank(rank=0, img=None, square=False):
    # Get image array
    width, height = img.size
    print("IMG SIze",img.size)
    data = list(img.getdata())
    print(img)
    A = np.array([data[offset:offset + width]  for offset in range(0, width * height, width)])
    print(A.shape)
    AtA = A.T @ A

    # Find eigenValues and eigenVectors
    values, vectors = la.eig(AtA)
    values_sort = np.sort(values)[::-1].real

    # Find V
    V = vectors[:, np.argsort(values)[::-1]].real
    print("V",V)
    # Choice eigenValues > 0
    for i in range(len(values_sort) - 1, -1, -1):
        if values_sort[i] <= 0:
            values_sort = np.delete(values_sort, i)
            V = np.delete(V, i, axis=1)

    # Find sigma
    sigma = np.sqrt(values_sort)

    # Create sigma array
    S = np.zeros((len(sigma), len(sigma)))
    S[:len(sigma), :len(sigma)] = np.diag(sigma)

    # Number of sigma
    r = len(S)
    print("SIGMA",sigma)
    # Find U
    U = A @ V[:, :r] / sigma

    # Approx image with rank = k
    k = rank
    app_matrix = U[:, :k] @ S[:k, :k] @ V.T[:k, :]

    # Error calculation
    error = error_calculation(sigma, rank, square)

    # Print result
    print("\n\nApprox image with rank =", k)
    print("\n   Size of A: {}".format(A.shape))
    print("   Size of AtA: {}".format(AtA.shape))
    print("\n   Error: {:.1f}%".format(error))
    print("   Max rank: {}".format(len(sigma)))
    # print("   Eigen values: {}".format(len(sigma)))
    # print("   Eigen vectors: {}".format(len(sigma)))
    print("\n   ==> A        = U{} * S{} * V.T{}".format(U.shape, S.shape, V.T.shape))
    print("   ==> Approx_A = U{} * S{} * V.T{}".format(U[:, :k].shape, S[:k, :k].shape, V.T[:k, :].shape))

    return app_matrix


def svd_error(error=0, img=None, square=False):
    error = error / 100

    # Get image array
    width, height = img.size
    data = list(img.getdata())
    A = np.array([data[offset:offset + width] for offset in range(0, width * height, width)])

    AtA = A.T @ A

    # Find eigenValues and eigenVectors
    values, vectors = la.eig(AtA)
    values_sort = np.sort(values)[::-1].real

    # Find V
    V = vectors[:, np.argsort(values)[::-1]].real

    # Choice eigenValues > 0
    for i in range(len(values_sort) - 1, -1, -1):
        if values_sort[i] <= 0:
            values_sort = np.delete(values_sort, i)
            V = np.delete(V, i, axis=1)

    # Find V
    V = vectors[:, np.argsort(values_sort)[::-1]].real

    # Find sigma array
    sigma = np.sqrt(values_sort)
    S = np.zeros((len(sigma), len(sigma)))
    S[:len(sigma), :len(sigma)] = np.diag(sigma)

    # Number of sigma
    r = len(S)
    U = A @ V[:, :r] / sigma

    k = rank_calculation(sigma, error, square)

    app_matrix = U[:, :k] @ S[:k, :k] @ V.T[:k, :]

    # Print result
    print("\n\nApprox image with error = {} %".format(error * 100))

    # print("Error at rank = 0: {}".format(error_rank0))
    print("\n   Size of A: {}".format(A.shape))
    print("   Size of AtA: {}".format(AtA.shape))
    print("\n   Rank: {}".format(k))
    print("   Max error: {}%".format(error_calculation(sigma, 0, square)))
    # print("   Eigen values: {}".format(len(sigma)))
    # print("   Eigen vectors: {}".format(len(sigma)))
    print("\n   ==> A       = U{} * S{} * V.T{}".format(U.shape, S.shape, V.T.shape))
    print("   ==> A_error = U{} * S{} * V.T{}".format(U[:, :k].shape, S[:k, :k].shape, V.T[:k, :].shape))

    return app_matrix


def rank_calculation(sigma, error, square=False):
    # Sigma**2 or not
    if square == False:
        h = 1
    else:
        h = 2

    # Calculate error of image
    k = 0
    app_sigma = 0
    sum_sigma = sum(sigma ** h)

    # Error percent at rank = 1
    error_rank0 = 1 - (sigma[0] ** h) / sum_sigma

    # Rank = k following error
    if error < error_rank0:
        for i in range(len(sigma)):
            app_sigma += sigma[i] ** h
            error_percent = 1 - app_sigma / sum_sigma
            if error_percent <= error:
                k = i
                return k
    else:
        return 0


def error_calculation(sigma, rank, square=False):
    # Sigma**2 or not
    if square == False:
        h = 1
    else:
        h = 2

    # Calculate error of image
    k = 0
    app_sigma = 0
    sum_sigma = sum(sigma ** h)
    max_rank = len(sigma)

    # return error base on rank

    for i in range(max_rank):
        if rank > max_rank:
            return 0
        else:
            app_sigma += sigma[i] ** h
            error_percent = 1 - app_sigma / sum_sigma
            if i == rank:
                return round(error_percent, 3) * 100



from copy import deepcopy

from numericalanalysis.matrix import Matrix


def copy(matrix):
    return deepcopy(matrix)


def identity(shape):
    eye = [[float(x == y) for x in range(shape)] for y in range(shape)]
    return Matrix(eye)


def zeros_vector(n):
    return [0.0 for i in range(n)]


def determinant(matrix):
    # TODO implement det function
    pass


def pivot(matrix):
    n = matrix.shape[0]
    identity_matrix = identity(n)

    for j in range(n):
        row = max(range(j, n), key=lambda i: abs(matrix[i][j]))
        if j != row:
            identity_matrix.matrix[j] = identity_matrix.matrix[row]
            identity_matrix.matrix[row] = identity_matrix.matrix[j]
    return identity_matrix

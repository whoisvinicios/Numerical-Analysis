from numericalanalysis.dimension_exception import DimensionErrorException
from numericalanalysis.matrix_helper import *

"""

LU decomposition (LU is stands for "lower-upper") factors a matrix as the product of lower triangular matrix
and a upper triangular matrix

Definition:
    Let A be a square matrix. An LU factorization refers to factor of A, with proper row and/or column ordering
    or permuations, into two factors -  a lower triangular matrix L and an upper triangluar matrix U:
    
        A = LU
        
    In the lower triangular matrix all elements above the diagonal are zero, in the upper triangular matrix, all
    the elements below the diagonal are zero. For example, for a 3 × 3 matrix A, its LU decomposition looks like this:
    
    | a11 a12 a13 |   | l11   0  0   |   | u11 u12 u13 |
    | a21 a22 a23 | = | l21 l22  0   | = |  0  u22 u23 |
    | a31 a32 a33 |   | l31 l32  l33 |   |  0   0  u33 |
    
    Ax = b
    
    1. First, we solve the equation Ly = Pb for y.
    2. Second, we solve the equation Ux = y for x.
"""


def lu_decomposition(matrix):
    """
    Perform the LU decomposition to the given matrix
    :param matrix: Matrix
    :return: Pivot matrix, Lower triangular matrix, Upper triangular matrix
    """
    if matrix.rows != matrix.cols:
        raise DimensionErrorException("Dimension Error", "The rows and column need to be equals")

    n = matrix.shape[0]
    l = identity(n)
    u = copy(matrix)

    for j in range(n):
        for i in range(j + 1, n):
            l[i][j] = u[i][j] / u[j][j]
            for k in range(j + 1, n):
                u[i][k] = u[i][k] - l[i][j] * u[j][k]
            u[i][j] = 0
    return l, u


def lu_decomposition_with_pivot(matrix):
    """
    Perform the LU decomposition with pivot to the given matrix
    :param matrix: Matrix
    :return: Pivot matrix, Lower triangular matrix, Upper triangular matrix
    """

    if matrix.rows != matrix.cols:
        raise DimensionErrorException("Dimension Error", "The rows and column need to be equals")

    n = matrix.shape[0]
    l = identity(n)
    u = copy(matrix)
    p = pivot(matrix)
    pa = p * matrix

    for j in range(n):

        for i in range(j + 1):
            s1 = sum(u[k][j] * l[i][k] for k in range(i))
            u[i][j] = pa[i][j] - s1

        for i in range(j, n):
            s2 = sum(u[k][j] * l[i][k] for k in range(j))
            l[i][j] = (pa[i][j] - s2) / u[j][j]

    return p, l, u

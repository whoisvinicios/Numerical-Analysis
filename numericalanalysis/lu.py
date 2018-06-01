from numericalanalysis.dimension_exception import DimensionErrorException
from numericalanalysis.matrix_helper import *


class LU:
    """Contais the logic to perform the l and u decomposition"""

    @staticmethod
    def factorize(matrix):
        """Perform the LU decomposition to the given matrix"""

        if matrix.rows != matrix.cols:
            raise DimensionErrorException("Dimension Error", "The rows and column need to be equals")

        n = matrix.shape[0]

        l = identity(n)
        u = copy(matrix)

        p = pivot(matrix)
        pa = p * matrix

    #     for j in range(n):
    #         for i in range(j + 1, n):
    #             l[i][j] = u[i][j] / u[j][j]
    #
    #             for k in range(j + 1, n):
    #                 u[i][k] = u[i][k] - l[i][j] * u[j][k]
    #             u[i][j] = 0
    #

        for j in range(n):

            for i in range(j + 1):
                s1 = sum(u[k][j] * l[i][k] for k in range(i))
                u[i][j] = pa[i][j] - s1

            for i in range(j, n):
                s2 = sum(u[k][j] * l[i][k] for k in range(j))
                l[i][j] = (pa[i][j] - s2) / u[j][j]

        return p, l, u

from dimension_exception import DimensionErrorException
from matrix import Matrix
from matrix_helper import MatrixHelper


class LU:
    """Contais the logic to perform the Lower and Upper decomposition"""

    @staticmethod
    def factorize(A, b):
        """Perform the LU decomposition to the given matrix"""

        if A.rows != A.cols:
            raise DimensionErrorException("Dimension Error", "The rows and column need to be equals")

        n = A.shape[0]
        U = MatrixHelper.copy(A)
        L = MatrixHelper.identity(n)


        # for j in range(n):
        #     for i in range(j + 1, n):
        #         L[i][j] = U[i][j] / U[j][j]
        #
        #         for k in range(j + 1, n):
        #             U[i][k] = U[i][k] - L[i][j] * U[j][k]
        #         U[i][j] = 0

        for j in range(n):
            for i in range(j + 1):
                s = sum(U[k][j] * L[i][k] for k in range(i))
                U[i][j] = A[i][j] - s
            for i in range(j, n):
                s = sum(U[k][j] * L[i][k] for k in range(j))
                L[i][j] = (A[i][j] - s) / U[j][j]
        return L, U

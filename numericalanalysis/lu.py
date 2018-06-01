from numericalanalysis.dimension_exception import DimensionErrorException
from numericalanalysis.matrix_helper import MatrixHelper


class LU:
    """Contais the logic to perform the Lower and Upper decomposition"""

    @staticmethod
    def factorize(A):
        """Perform the LU decomposition to the given matrix"""

        if A.rows != A.cols:
            raise DimensionErrorException("Dimension Error", "The rows and column need to be equals")

        n = A.shape[0]
        L = MatrixHelper.identity(n)
        U = MatrixHelper.copy(A)

        for j in range(n):
            for i in range(j + 1, n):
                L[i][j] = U[i][j] / U[j][j]

                for k in range(j + 1, n):
                    U[i][k] = U[i][k] - L[i][j] * U[j][k]
                U[i][j] = 0

        return L, U

    @staticmethod
    def solve(L, U, b):
        """
        TODO: Fix that
        """
        n = L.shape[0]

        y = MatrixHelper.zeros_vector(n)
        x = MatrixHelper.zeros_vector(n)

        y[0] = b[0] / L[0][0]
        for i in range(1, n):
            sum = 0.0
            for j in range(i):
                sum += L[i][j] * y[j]
            y[i] = (b[i] - sum) / L[i][i]

        x[n - 1] = y[n - 1] / U[n - 1][n - 1]
        for i in range(n - 1, -1, -1):
            sum = y[i]
            for j in range(i + 1, n):
                sum = sum - U[i][j] * x[j]
            x[i] = sum / U[i][i]

        return y, x

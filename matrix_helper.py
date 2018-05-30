from copy import deepcopy

from matrix import Matrix


class MatrixHelper:
    """This class constains some helper methods for Matrix class"""

    @staticmethod
    def determinant(matrix):
        return None

    @staticmethod
    def copy(matrix):
        return deepcopy(matrix)

    @staticmethod
    def identity(shape):
        eye = [[1.0 if x == y else 0.0 for x in range(shape)] for y in range(shape)]
        m = Matrix(eye)
        return m
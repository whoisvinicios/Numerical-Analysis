from copy import deepcopy

from numericalanalysis.matrix import Matrix
from numericalanalysis.dimension_exception import DimensionErrorException

import itertools


class MatrixHelper:
    """This class constains some helper methods for Matrix class"""
    @staticmethod
    def copy(matrix):
        return deepcopy(matrix)

    @staticmethod
    def identity(shape):
        eye = [[1.0 if x == y else 0.0 for x in range(shape)] for y in range(shape)]
        m = Matrix(eye)
        return m

    @staticmethod
    def zeros_vector(n):
        return [0.0 for i in range(n)]


def determinant(matrix):
    pass
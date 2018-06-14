import random
from itertools import chain

from numericalanalysis.dimension_exception import DimensionErrorException


class Matrix:
    def __init__(self, matrix):
        self._matrix = matrix
        self._rows = len(matrix)
        self._cols = len(matrix[0])

    @property
    def matrix(self):
        return self._matrix

    @property
    def rows(self):
        return self._rows

    @property
    def cols(self):
        return self._cols

    @property
    def shape(self):
        shape = (self._rows, self._cols)
        return shape

    def __repr__(self):
        return str(self._matrix)

    def __str__(self):
        return str(self._matrix)

    def __getitem__(self, key):
        return self._matrix[key]

    def __iter__(self):
        return chain.from_iterable(self._matrix)

    def __add__(self, other):
        if self._shape != other.shape:
            raise DimensionErrorException()
        m = Matrix([[self._matrix[x][y] + other.matrix[x][y] for y in range(self._cols)] for x in range(self._rows)])
        return m

    def __sub__(self, other):
        if self._shape != other.shape:
            raise DimensionErrorException()
        m = Matrix([[self._matrix[x][y] - other.matrix[x][y] for y in range(self._cols)] for x in range(self._rows)])
        return m

    def __mul__(self, other):
        # TODO implements multiplication by scalar
        if self._cols != other.rows:
            raise DimensionErrorException("Rows must be equals to cols", "Dimension Error")
        x = self.matrix
        y = other.matrix
        matrix = [[sum(x * y for x, y in zip(x_row, y_col)) for y_col in zip(*y)] for x_row in x]
        return Matrix(matrix)

    def __eq__(self, other):
        for x in range(self._rows):
            for y in range(self._cols):
                if self._matrix[x][y] != other[x][y]:
                    return False
        return True

    @staticmethod
    def generate(shape):
        if type(shape) != tuple:
            raise TypeError("Must be a tuple")
        m = [[random.random() for _ in range(shape[1])] for _ in range(shape[0])]
        return Matrix(m)

from itertools import chain

from dimension_exception import DimensionErrorException


class Matrix:
    """This class represents a Matrix"""

    def __init__(self, matrix):
        self._matrix = matrix
        self._rows = len(matrix)
        self._cols = len(matrix[0])
        self._shape = (self._rows, self._cols)

    @property
    def matrix(self):
        """Get the matrix"""
        return self._matrix

    @property
    def rows(self):
        """Get rows numbers"""
        return self._rows

    @property
    def cols(self):
        """Get cols numbers"""
        return self._cols

    @property
    def shape(self):
        """Get the shape of matrix"""
        return self._shape

    def __repr__(self):
        return str(self._matrix)

    def __getitem__(self, key):
        return self._matrix[key]

    def __iter__(self):
        return chain.from_iterable(self._matrix)

    def __add__(self, other):
        if self._shape != other.shape:
            raise DimensionErrorException()
        m = [[self._matrix[x][y] + other.matrix[x][y] for y in range(self._cols)] for x in range(self._rows)]
        return m

    def __sub__(self, other):
        if self._shape != other.shape:
            raise DimensionErrorException()
        m = [[self._matrix[x][y] - other.matrix[x][y] for y in range(self._cols)] for x in range(self._rows)]
        return m

    def __mul__(self, other):
        if self._rows != other.cols:
            raise DimensionErrorException("Rows must be equals to cols", "Dimension Error")

from itertools import chain

from numericalanalysis.dimension_exception import DimensionErrorException


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
        if self._cols != other.rows:
            raise DimensionErrorException("Rows must be equals to cols", "Dimension Error")
        x = self.matrix
        y = other.matrix
        return [[sum(x * y for x, y in zip(x_row, y_col)) for y_col in zip(*y)] for x_row in x]

    def __eq__(self, other):
        for x in range(self._rows):
            for y in range(self._cols):
                if self._matrix[x][y] != other[x][y]:
                    return False
        return True
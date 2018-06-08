from itertools import chain

from numericalanalysis.dimension_exception import DimensionErrorException


class Matrix:
    """
    This class represents a Matrix and implements some
    mathematical operations that can be done with matrixes
    """

    def __init__(self, matrix):
        """
        Constructor
        :param matrix: matrix in format [[1, 2, 3], [3, 2, 1]]
        """
        self._matrix = matrix
        self._rows = len(matrix)
        self._cols = len(matrix[0])
        self._shape = (self._rows, self._cols)

    @property
    def matrix(self):
        """
        Get the matrix
        :return: the matrix attribute
        """
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

    def __str__(self):
        return str(self._matrix)

    def __getitem__(self, key):
        return self._matrix[key]

    def __iter__(self):
        return chain.from_iterable(self._matrix)

    def __add__(self, other):
        """
        Adds two matrix
        :param other:
        :return: added matrix
        """
        if self._shape != other.shape:
            raise DimensionErrorException()
        m = Matrix([[self._matrix[x][y] + other.matrix[x][y] for y in range(self._cols)] for x in range(self._rows)])
        return m

    def __sub__(self, other):
        """
        Subtract two matrix
        :param other:
        :return: matrix subtracted
        """
        if self._shape != other.shape:
            raise DimensionErrorException()
        m = Matrix([[self._matrix[x][y] - other.matrix[x][y] for y in range(self._cols)] for x in range(self._rows)])
        return m

    def __mul__(self, other):
        """
        Multiplies two matrix, the number of columns of the first matrix must be equal to the number of rows of the
        second matrix

        iterative implementation

        for i in range(len(X)):
            # iterate through columns of Y
            for j in range(len(Y[0])):
                # iterate through rows of Y
                    for k in range(len(Y)):
                        result[i][j] += X[i][k] * Y[k][j]

        :param other: Matrix
        :return: matrix multiplied
        """

        # TODO implements multiplication by scalar
        # FIXME
        if type(other) is int:
            matrix = [[other * self._matrix[x][y] for y in range(self._cols)] for x in range(self._rows)]
            return Matrix(matrix)
        else:
            if self._cols != other.rows:
                raise DimensionErrorException("Rows must be equals to cols", "Dimension Error")
            x = self.matrix
            y = other.matrix
            matrix = [[sum(x * y for x, y in zip(x_row, y_col)) for y_col in zip(*y)] for x_row in x]
            return Matrix(matrix)

    def __eq__(self, other):
        """
        Compare two matrix
        :param other:
        :return:
        """
        for x in range(self._rows):
            for y in range(self._cols):
                if self._matrix[x][y] != other[x][y]:
                    return False
        return True

a = Matrix([[1, 2, 3], [3, 2, 1]])
c = Matrix([[1, 2, 3], [3, 2, 1]])
b = 2 * a

print(b)
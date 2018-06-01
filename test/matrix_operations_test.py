import unittest

from numericalanalysis.matrix import Matrix


class MatrixOperationsTest(unittest.TestCase):

    def setUp(self):
        self.x = Matrix([[12, 7, 3], [4, 5, 6], [7, 8, 9]])
        self.y = Matrix([[5, 8, 1, 2], [6, 7, 3, 0], [4, 5, 9, 1]])

    def test_matrix_multiplication(self):
        z = Matrix([[114, 160, 60, 27], [74, 97, 73, 14], [119, 157, 112, 23]])
        result = self.x * self.y
        self.assertEqual(z, result)


if __name__ == "__main__":
    unittest.main()
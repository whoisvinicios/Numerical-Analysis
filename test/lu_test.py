import unittest

from numericalanalysis.lu import LU
from numericalanalysis.matrix import Matrix


class LUTest(unittest.TestCase):

    def setUp(self):
        self.x = Matrix([[2., 1., 1.], [1., 3., 2.], [1., 0., 0.]])
        self.y = Matrix([[1, 1, 1], [2, 1, -1], [2, -1, 1]])

    def test_x_lu_decomp(self):
        l, u = LU.factorize(self.x)
        self.assertEqual(l.matrix, [[1.0, 0.0, 0.0], [2.0, 1.0, 0.0], [2.0, 3.0, 1.0]])
        self.assertEqual(u.matrix, [[1, 1, 1], [0, -1.0, -3.0], [0, 0, 8.0]])

    # def test_y_lu_decomp(self):
    #     l, u = LU.factorize(self.y)
    #     self.assertEqual(l.matrix, [[1., 0., 0.], [0.5, 1., 0.], [0.5 - 0.2, 1.]])
    #     self.assertEqual(u.matrix, [[2., 1., 1.], [0., 2.5, 1.5], [0., 0., -0.2]])


if __name__ == "__main__":
    unittest.main()

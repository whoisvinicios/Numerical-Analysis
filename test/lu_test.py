import unittest

from numericalanalysis.lu import lu_decomposition
from numericalanalysis.matrix import Matrix


class LUTest(unittest.TestCase):

    def setUp(self):
        self.x = Matrix([[1,2,1], [1,4,3], [0,0,5]])

    def test_x_lu_decomp(self):
        l, u = lu_decomposition(self.x)
        y = l * u
        self.assertEqual(self.x, y)


if __name__ == "__main__":
    unittest.main()

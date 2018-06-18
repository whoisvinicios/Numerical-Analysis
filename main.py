from numericalanalysis.dimension_exception import DimensionErrorException
from numericalanalysis.linear_solver import *
from numericalanalysis.lu import lu_decomposition
from numericalanalysis.matrix import Matrix
from numericalanalysis.vector import Vector


def main():
    try:
        # a = Matrix([
        #     [1, 2, 1],
        #     [1, 4, 3],
        #     [0, 0, 5]])
        # b = Vector([1, 2, 5])

        a = Matrix([[4, 1, 2, -1],
                    [3, 6, -1, 2],
                    [2, -1, 5, -3],
                    [4, 1, -3, -8]])
        b = Vector([2, -1, 3, 2])

        l, u = lu_decomposition(a)
        y, x = solve(l, u, b)

        # print("A: {}".format(a))
        # print("L: {}".format(l))
        # print("y: {}".format(y))
        # print("U: {}".format(u))
        print("x: {}".format(x))
    except DimensionErrorException as e:
        print(e)


if __name__ == "__main__":
    main()

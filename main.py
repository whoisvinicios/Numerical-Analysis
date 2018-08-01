from numericalanalysis.dimension_exception import DimensionErrorException
from numericalanalysis.linear_solver import *
from numericalanalysis.lu import lu_decomposition, print_system, print_matrix
from numericalanalysis.matrix import Matrix
from numericalanalysis.vector import Vector


def main():
    try:
        a = Matrix([
            [1, 2, 4, 4],
            [1, 1, 1, 2],
            [1, 2, 1, 1],
            [0, 0, 2, 3]])
        b = Vector([68, 24, 26, 32])

        # a = Matrix([[4, 1, 2, -1],
        #             [3, 6, -1, 2],
        #             [2, -1, 5, -3],
        #             [4, 1, -3, -8]])
        # b = Vector([2, -1, 3, 2])

        l, u = lu_decomposition(a)
        y, x = solve(l, u, b)

        # print("A: {}".format(a))
        # print("b: {}".format(b))
        # print()
        print_system(a, b)
        print()

        print_matrix(l)
        print()

        print_matrix(u)
        print()

        # print_system(u, x)
        print("x: {}".format(x))
        print()
    except DimensionErrorException as e:
        print(e)


if __name__ == "__main__":
    main()

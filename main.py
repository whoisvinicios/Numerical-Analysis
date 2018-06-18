from numericalanalysis.dimension_exception import DimensionErrorException
from numericalanalysis.linear_solver import solve
from numericalanalysis.lu import lu_decomposition
from numericalanalysis.matrix import Matrix
from numericalanalysis.vector import Vector


def main():
    try:
        a = Matrix([[1,2,1], [1,4,3], [0,0,5]])
        b = Vector([1, 2, 5])

        l, u = lu_decomposition(a)
        y, x = solve(l, u, b)

        print("A: {}".format(a))
        print("L: {}".format(l))
        print("y: {}".format(y))
        print("U: {}".format(u))
        print("x: {}".format(x))
    except DimensionErrorException as e:
        print(e)


if __name__ == "__main__":
    main()

from numericalanalysis.dimension_exception import DimensionErrorException
from numericalanalysis.lu import lu
from numericalanalysis.matrix import Matrix


def main():
    try:
        a = Matrix([
            [1, 1, 1],
            [2, 1, -1],
            [2, -1, 1]])

        # b = Matrix([[-2, 1, 3]])
        b = [-2, 1, 3]

        p, l, u = lu(a)
        # y, x = solve(l, u, b)
        print(l)
        print(u)

        print(y)
        print(x)
    except DimensionErrorException as e:
        print(e)


if __name__ == "__main__":
    main()

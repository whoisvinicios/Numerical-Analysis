from numericalanalysis.dimension_exception import DimensionErrorException
from numericalanalysis.lu import LU
from numericalanalysis.matrix import Matrix


def main():
    try:
        A = Matrix([
            [1, 1, 1],
            [2, 1, -1],
            [2, -1, 1]])

        # b = Matrix([[-2, 1, 3]])
        b = [-2, 1, 3]

        P, L, U = LU.factorize(A)
        y, x = LU.solve(L, U, b)
        print(L)
        print(U)

        print(y)
        print(x)
    except DimensionErrorException as e:
        print(e)


if __name__ == "__main__":
    main()

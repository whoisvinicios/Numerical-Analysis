from numericalanalysis.dimension_exception import DimensionErrorException
from numericalanalysis.lu import LU
from numericalanalysis.matrix import Matrix


def main():
    try:
        A = Matrix([
            [1, 1, 1],
            [2, 1, -1],
            [2, -1, 1]])

        b = Matrix([[-2, 1, 3]])

        L, U = LU.factorize(A, b)
        print(L)
        print(U)
    except DimensionErrorException as e:
        print(e)


if __name__ == "__main__":
    main()

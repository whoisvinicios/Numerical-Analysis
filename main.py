from numericalanalysis.dimension_exception import DimensionErrorException
from numericalanalysis.lu import lu_decomposition
from numericalanalysis.matrix import Matrix


def main():
    try:
        a = Matrix([[1, 1, 1], [2, 1, -1], [2, -1, 1]])

        l, u = lu_decomposition(a)
        print(l)
        print(u)
    except DimensionErrorException as e:
        print(e)


if __name__ == "__main__":
    main()

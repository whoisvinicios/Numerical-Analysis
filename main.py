from numericalanalysis.dimension_exception import DimensionErrorException
from numericalanalysis.lu import lu_decomposition
from numericalanalysis.matrix import Matrix


def main():
    try:
        #a = Matrix([[1,2,1], [1,4,3], [0,0,5]])
        #b = Matrix([[1, 2, 3]])

        a = Matrix.generate_matrix((100, 100), 0, 100)
        l, u = lu_decomposition(a)

        c = l * u

        print("A: {}".format(a))
        print("L: {}".format(l))
        print("U: {}".format(u))
        print("L x U = {}".format(c))
    except DimensionErrorException as e:
        print(e)


if __name__ == "__main__":
    main()

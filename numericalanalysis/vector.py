from numericalanalysis.matrix import Matrix


class Vector(Matrix):

    def __init__(self, vector, dtype="row"):
        super().__init__(vector)

        self._type = dtype

        if dtype == "row":
            self._shape = (len(vector), 0)
        else:
            self._shape = (0, len(vector))

    @property
    def shape(self):
        return self._shape

    @property
    def vector(self):
        return self._matrix[0]

    def __eq__(self, other):
        pass

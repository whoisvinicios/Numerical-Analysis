class Vector:

    def __init__(self, vector):
        self._vector = vector
        self._len = len(vector)

    @property
    def shape(self):
        return self._shape

    @property
    def vector(self):
        return self._matrix[0]

    def __eq__(self, other):
        pass

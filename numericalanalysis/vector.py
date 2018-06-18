class Vector:

    def __init__(self, vector):
        self._vector = vector
        self._len = len(vector)

    @property
    def shape(self):
        return self._shape

    @property
    def vector(self):
        return self._vector

    def __getitem__(self, key):
        return self._vector[key]

    def __eq__(self, other):
        pass

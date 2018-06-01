class DimensionErrorException(Exception):
    """Exception that be raisase when matrix have some dimension error"""

    def __init__(self, message, errors):
        super().__init__(message)
        self.errors = errors

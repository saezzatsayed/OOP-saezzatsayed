# creating class sample.
class Sample(list):
    """
    Represents a sample of data.
    Inherits from the built-in list class.
    """

    def __init__(self, data=None):
        """
        Initializes a Sample object with the given data (optional).
        """
        super().__init__(data or [])
        self._n = len(self)
        self._data = data

    # Setting data.
    def set_data(self, data):
        self._data = data

    # setting n and sample.
    def set_sample(self, n, sample):
        self._n = n
        self._data = sample

    # function to return private variable "data".
    def get_data(self):
        return self._data

    # function to return private variables "n", "sample".
    def get_sample(self):
        return (self._n, self._data)

    # function to returns the value of the method "min".
    def get_min(self):
        return min(self._data)

    # function to returns the value of the method "max".
    def get_max(self):
        return max(self._data)

    # function to returns the value of the method "range" (max - min).
    def get_range(self):
        return max(self._data) - min(self._data)
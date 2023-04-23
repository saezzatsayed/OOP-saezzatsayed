class movie_name:
    def __init__(self, name = "nothing"):
        self._name = name 

    def get_name(self):
        return self._name

    def set_name(self, n):
        self._name = n

class movie_cap:
    def __init__(self, value = "0"):
        self._value = value 

    def get_value(self):
        return self._value

    def set_value(self, v):
        self._value = v
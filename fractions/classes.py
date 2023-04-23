class fraction:
    def __init__(self, x: int = 0, y: int = 0):
        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def set_x(self, m):
        self._x = m

    def set_y(self, n):
        self._y = n

class reminder:
    def __init__(self, whole: int = 0, rem: int = 0):
        self._whole = whole
        self._rem = rem

    def get_whole(self):
        return self._whole

    def get_rem(self):
        return self._rem

    def set_whole(self, m):
        self._whole = m

    def set_rem(self, n):
        self._rem = n
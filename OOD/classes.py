from typing import List

def polygon_area(x, y, n):
    '''Takes a list of x and y values
       Takes the number of pairs
       Returns calculated area
    '''
    area = 0.0

    j = n - 1
    for i in range(0,n):
        area += (float(x[j])+float(x[i])) * (float(y[j])-float(y[i]))
        j = i
    
    return float(abs(area/2.0))

class Polygon:
    '''Takes number of pairs
       Takes list of x values
       Takes list of y values
    '''
    def __init__(self) -> None:
        self.__no_of_pairs = 0
        self.__x_vals: List[int] = []
        self.__y_vals: List[int] = []

    def set_no_of_pairs(self, value: int) -> None:
        self.__no_of_pairs = value

    def get_no_of_pairs(self) -> int:
        return self.__no_of_pairs

    def set_x_vals(self, values: List[int]) -> None:
        self.__x_vals = values

    def get_x_vals(self) -> List[int]:
        return self.__x_vals

    def set_y_vals(self, values: List[int]) -> None:
        self.__y_vals = values

    def get_y_vals(self) -> List[int]:
        return self.__y_vals
from typing import List

def polygon_area(x: List[float], y: List[float], n: int) -> float:
    '''
    Calculate the area of a polygon given its x and y values.
    
    Args:
        x: A list of x-coordinate values.
        y: A list of y-coordinate values.
        n: The number of pairs of coordinates.
    
    Returns:
        The calculated area of the polygon as a float.
    '''
    area: float = 0.0

    j: int = n - 1
    for i in range(0, n):
        area += (float(x[j]) + float(x[i])) * (float(y[j]) - float(y[i]))
        j = i
    
    return float(abs(area / 2.0))

class Polygon:
    '''
    Represents a polygon with its number of pairs and coordinate values.

    Attributes:
        __no_of_pairs (int): The number of coordinate pairs.
        __x_vals (List[int]): The list of x-coordinate values.
        __y_vals (List[int]): The list of y-coordinate values.
    '''

    def __init__(self) -> None:
        '''
        Initialize a Polygon object.
        '''
        self.__no_of_pairs: int = 0
        self.__x_vals: List[int] = []
        self.__y_vals: List[int] = []

    def set_no_of_pairs(self, value: int) -> None:
        '''
        Set the number of coordinate pairs for the polygon.

        Args:
            value (int): The number of coordinate pairs.
        '''
        self.__no_of_pairs = value

    def get_no_of_pairs(self) -> int:
        '''
        Get the number of coordinate pairs for the polygon.

        Returns:
            The number of coordinate pairs as an integer.
        '''
        return self.__no_of_pairs

    def set_x_vals(self, values: List[int]) -> None:
        '''
        Set the list of x-coordinate values for the polygon.

        Args:
            values (List[int]): The list of x-coordinate values.
        '''
        self.__x_vals = values

    def get_x_vals(self) -> List[int]:
        '''
        Get the list of x-coordinate values for the polygon.

        Returns:
            The list of x-coordinate values.
        '''
        return self.__x_vals

    def set_y_vals(self, values: List[int]) -> None:
        '''
        Set the list of y-coordinate values for the polygon.

        Args:
            values (List[int]): The list of y-coordinate values.
        '''
        self.__y_vals = values

    def get_y_vals(self) -> List[int]:
        '''
        Get the list of y-coordinate values for the polygon.

        Returns:
            The list of y-coordinate values.
        '''
        return self.__y_vals

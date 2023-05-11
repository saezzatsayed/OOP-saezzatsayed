Module classes
==============

Functions
---------

    
`polygon_area(x: List[float], y: List[float], n: int) ‑> float`
:   Calculate the area of a polygon given its x and y values.
    
    Args:
        x: A list of x-coordinate values.
        y: A list of y-coordinate values.
        n: The number of pairs of coordinates.
    
    Returns:
        The calculated area of the polygon as a float.

Classes
-------

`Polygon()`
:   Represents a polygon with its number of pairs and coordinate values.
    
    Attributes:
        __no_of_pairs (int): The number of coordinate pairs.
        __x_vals (List[int]): The list of x-coordinate values.
        __y_vals (List[int]): The list of y-coordinate values.
    
    Initialize a Polygon object.

    ### Methods

    `get_no_of_pairs(self) ‑> int`
    :   Get the number of coordinate pairs for the polygon.
        
        Returns:
            The number of coordinate pairs as an integer.

    `get_x_vals(self) ‑> List[int]`
    :   Get the list of x-coordinate values for the polygon.
        
        Returns:
            The list of x-coordinate values.

    `get_y_vals(self) ‑> List[int]`
    :   Get the list of y-coordinate values for the polygon.
        
        Returns:
            The list of y-coordinate values.

    `set_no_of_pairs(self, value: int) ‑> None`
    :   Set the number of coordinate pairs for the polygon.
        
        Args:
            value (int): The number of coordinate pairs.

    `set_x_vals(self, values: List[int]) ‑> None`
    :   Set the list of x-coordinate values for the polygon.
        
        Args:
            values (List[int]): The list of x-coordinate values.

    `set_y_vals(self, values: List[int]) ‑> None`
    :   Set the list of y-coordinate values for the polygon.
        
        Args:
            values (List[int]): The list of y-coordinate values.
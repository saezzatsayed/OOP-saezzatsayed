class MovieName:
    def __init__(self, name: str = "nothing"):
        """
        Initialize a MovieName object.

        Args:
            name (str): The name of the movie. Defaults to "nothing".
        """
        self._name = name

    def get_name(self) -> str:
        """
        Get the name of the movie.

        Returns:
            str: The name of the movie.
        """
        return self._name

    def set_name(self, name: str):
        """
        Set the name of the movie.

        Args:
            name (str): The new name of the movie.
        """
        self._name = name


class MovieCap:
    def __init__(self, value: str = "0"):
        """
        Initialize a MovieCap object.

        Args:
            value (str): The cap value of the movie. Defaults to "0".
        """
        self._value = value

    def get_value(self) -> str:
        """
        Get the cap value of the movie.

        Returns:
            str: The cap value of the movie.
        """
        return self._value

    def set_value(self, value: str):
        """
        Set the cap value of the movie.

        Args:
            value (str): The new cap value of the movie.
        """
        self._value = value

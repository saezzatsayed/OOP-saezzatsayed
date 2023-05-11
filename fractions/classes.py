class Fraction:
    """
    Represents a fraction with a numerator and denominator.
    """

    def __init__(self, numerator: int = 0, denominator: int = 0):
        """
        Initializes a fraction object with the given numerator and denominator.
        """
        self._numerator = numerator
        self._denominator = denominator

    def get_numerator(self) -> int:
        """
        Returns the numerator of the fraction.
        """
        return self._numerator

    def get_denominator(self) -> int:
        """
        Returns the denominator of the fraction.
        """
        return self._denominator

    def set_numerator(self, numerator: int):
        """
        Sets the numerator of the fraction.
        """
        self._numerator = numerator

    def set_denominator(self, denominator: int):
        """
        Sets the denominator of the fraction.
        """
        self._denominator = denominator


class Reminder:
    """
    Represents a mixed fraction with a whole number and a remainder.
    """

    def __init__(self, whole: int = 0, remainder: int = 0):
        """
        Initializes a Reminder object with the given whole number and remainder.
        """
        self._whole = whole
        self._remainder = remainder

    def get_whole(self) -> int:
        """
        Returns the whole number of the mixed fraction.
        """
        return self._whole

    def get_remainder(self) -> int:
        """
        Returns the remainder number of the mixed fraction.
        """
        return self._remainder

    def set_whole(self, whole: int):
        """
        Sets the whole number of the mixed fraction.
        """
        self._whole = whole

    def set_remainder(self, remainder: int):
        """
        Sets the remainder number of the mixed fraction.
        """
        self._remainder = remainder

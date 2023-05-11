class MorseCodeConverter:
    """
    Class for converting text to Morse code and vice versa.
    """

    _morse_code = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
        'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'
    }

    def get_morse_code(self) -> dict:
        """
        Get the dictionary of Morse code mappings.
        """
        return MorseCodeConverter._morse_code

    def set_morse_code(self, morse_code: dict):
        """
        Set the dictionary of Morse code mappings.
        """
        MorseCodeConverter._morse_code = morse_code

    def convert_to_morse_code(self, s: str) -> str:
        """
        Convert the input string to Morse code.

        Args:
            s: The input string to be converted.

        Returns:
            The converted Morse code string.
        """
        morse_string = ''
        for char in s:
            if char.upper() in MorseCodeConverter._morse_code:
                morse_string += MorseCodeConverter._morse_code[char.upper()]
        return morse_string


class MorsePalindromeChecker:
    """
    Class for checking if a string is a palindrome in Morse code.
    """

    def __init__(self):
        self.morse_converter = MorseCodeConverter()

    def is_morse_code_palindrome(self, s: str) -> int:
        """
        Check if the input string is a palindrome in Morse code.

        Args:
            s: The input string to be checked.

        Returns:
            1 if the string is a Morse code palindrome, 0 otherwise.
        """
        if s.isspace():
            return 0

        # Convert input string to Morse code
        morse_string = self.morse_converter.convert_to_morse_code(s)

        # Check if the Morse code string is a palindrome
        morse_string = morse_string.replace(' ', '')  # remove spaces to check for palindrome
        return int(morse_string == morse_string[::-1])  # return 1 or 0 directly, without using if-else statement

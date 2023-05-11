Module classes
==============

Classes
-------

`MorseCodeConverter()`
:   Class for converting text to Morse code and vice versa.

    ### Methods

    `convert_to_morse_code(self, s: str) ‑> str`
    :   Convert the input string to Morse code.
        
        Args:
            s: The input string to be converted.
        
        Returns:
            The converted Morse code string.

    `get_morse_code(self) ‑> dict`
    :   Get the dictionary of Morse code mappings.

    `set_morse_code(self, morse_code: dict)`
    :   Set the dictionary of Morse code mappings.

`MorsePalindromeChecker()`
:   Class for checking if a string is a palindrome in Morse code.

    ### Methods

    `is_morse_code_palindrome(self, s: str) ‑> int`
    :   Check if the input string is a palindrome in Morse code.
        
        Args:
            s: The input string to be checked.
        
        Returns:
            1 if the string is a Morse code palindrome, 0 otherwise.
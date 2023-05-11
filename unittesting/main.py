
     
from classes import MorsePalindromeChecker, MorseCodeConverter


def main():
    """
    Main function to execute when the module is run directly.
    """
    morse_checker = MorsePalindromeChecker()
    s = input("Enter a Morse code string: ").strip()
    print(morse_checker.is_morse_code_palindrome(s))
    print("This file is being run directly")


if __name__ == '__main__':
    main()
else:
    print("This is an imported file")

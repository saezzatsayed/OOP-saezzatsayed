from classes import MorsePalindromeChecker, MorseCodeConverter

morse_checker = MorsePalindromeChecker()
s = input().strip()
print(morse_checker.is_morse_code_palindrome(s))

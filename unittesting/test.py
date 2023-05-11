import unittest
from classes import MorsePalindromeChecker, MorseCodeConverter
import unittest
from hypothesis import given
from hypothesis.strategies import text

class TestMorsePalindromeChecker(unittest.TestCase):

    def setUp(self):
        self.morse_checker = MorsePalindromeChecker()

    def test_empty_string(self):
        result = self.morse_checker.is_morse_code_palindrome('')
        self.assertEqual(result, 1)

    def test_palindrome_string(self):
        result = self.morse_checker.is_morse_code_palindrome('-.--.--.')
        self.assertEqual(result, 1)

    def test_non_palindrome_string(self):
        result = self.morse_checker.is_morse_code_palindrome('-.--.--.-')
        self.assertEqual(result, 1)

    @given(text())
    def test_is_morse_code_palindrome(self, input_string):
        morse_checker = MorsePalindromeChecker()
        result = morse_checker.is_morse_code_palindrome(input_string)
        self.assertIsInstance(result, int)

if __name__ == '__main__':
    unittest.main()

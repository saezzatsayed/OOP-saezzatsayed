import unittest
from classes import Fraction, Reminder
from hypothesis import given
from hypothesis import strategies as st
import coverage


# Create a coverage object
cov = coverage.Coverage()

# Start coverage measurement
cov.start()

class TestFraction(unittest.TestCase):

    def test_get_numerator(self):
        fraction = Fraction(3, 5)
        self.assertEqual(fraction.get_numerator(), 3)

    def test_get_denominator(self):
        fraction = Fraction(3, 5)
        self.assertEqual(fraction.get_denominator(), 5)

    def test_set_numerator(self):
        fraction = Fraction()
        fraction.set_numerator(4)
        self.assertEqual(fraction.get_numerator(), 4)

    @given(st.integers(), st.integers(min_value=1))
    def test_fraction_equivalence(self, numerator, denominator):
        fraction = Fraction(numerator, denominator)
        self.assertEqual(fraction.get_numerator(), numerator)
        self.assertEqual(fraction.get_denominator(), denominator)

class TestReminder(unittest.TestCase):

    def test_get_whole(self):
        reminder = Reminder(2, 3)
        self.assertEqual(reminder.get_whole(), 2)

    def test_get_remainder(self):
        reminder = Reminder(2, 3)
        self.assertEqual(reminder.get_remainder(), 3)

    def test_set_remainder(self):
        reminder = Reminder()
        reminder.set_remainder(5)
        self.assertEqual(reminder.get_remainder(), 5)

    @given(st.integers(), st.integers())
    def test_reminder_equivalence(self, whole, remainder):
        reminder = Reminder(whole, remainder)
        self.assertEqual(reminder.get_whole(), whole)
        self.assertEqual(reminder.get_remainder(), remainder)

if __name__ == '__main__':
    # Stop coverage measurement
    cov.stop()
    # Generate HTML report
    cov.html_report(directory='coverage_html_report')
    # Run the tests
    unittest.main()

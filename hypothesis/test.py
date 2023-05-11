import unittest
from unittest.mock import patch
from hypothesis import given
from hypothesis.strategies import text
import sys
import coverage
from io import StringIO
from classes import MovieName, MovieCap


class TestMovieName(unittest.TestCase):
    def test_get_name(self):
        name = "Avengers"
        movie = MovieName(name)
        self.assertEqual(movie.get_name(), name)

    def test_set_name(self):
        name = "Avengers"
        new_name = "Iron Man"
        movie = MovieName(name)
        movie.set_name(new_name)
        self.assertEqual(movie.get_name(), new_name)

    def test_default_name(self):
        movie = MovieName()
        self.assertEqual(movie.get_name(), "nothing")


class TestMovieCap(unittest.TestCase):
    def test_get_value(self):
        value = "2 hours"
        movie = MovieCap(value)
        self.assertEqual(movie.get_value(), value)

    def test_set_value(self):
        value = "2 hours"
        new_value = "1 hour 30 minutes"
        movie = MovieCap(value)
        movie.set_value(new_value)
        self.assertEqual(movie.get_value(), new_value)

    def test_default_value(self):
        movie = MovieCap()
        self.assertEqual(movie.get_value(), "0")


class TestMovieNameHypothesis(unittest.TestCase):
    @given(text())
    def test_set_name(self, name):
        movie = MovieName()
        movie.set_name(name)
        self.assertEqual(movie.get_name(), name)


if __name__ == '__main__':
    # Patch stdin and stdout
    with patch('builtins.input', return_value='Iron Man'), \
            patch('sys.stdout', new_callable=StringIO) as mock_stdout:
        # Run the tests
        unittest.main()

    # Generate coverage report
    cov = coverage.Coverage()
    cov.start()
    unittest.main(exit=False)
    cov.stop()
    cov.save()

    # Generate HTML coverage report
    cov.html_report(directory='coverage_html')

import unittest
from classes import Sample
from unittest.mock import patch
import io
from hypothesis import given
import hypothesis.strategies as st
import coverage

cov = coverage.Coverage()
cov.start()

class TestSample(unittest.TestCase):

    @patch('builtins.input', return_value='1 2 3 4 5')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_set_data(self, mock_stdout, mock_input):
        sample = Sample()
        sample.set_data(list(map(int, input().split())))
        self.assertEqual(sample.get_data(), [1, 2, 3, 4, 5])
        self.assertEqual(mock_stdout.getvalue().strip(), "")

    @patch('builtins.input', return_value='5 1 2 3 4 5')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_set_sample(self, mock_stdout, mock_input):
        sample = Sample()
        n = int(input().split()[0])
        sample.set_sample(n, list(map(int, input().split()[1:])))
        self.assertEqual(sample.get_sample(), (5, [1, 2, 3, 4, 5]))
        self.assertEqual(mock_stdout.getvalue().strip(), "")

    def test_get_min(self):
        sample = Sample([4, 1, 3, 2, 5])
        self.assertEqual(sample.get_min(), 1)

    def test_get_max(self):
        sample = Sample([4, 1, 3, 2, 5])
        self.assertEqual(sample.get_max(), 5)

    def test_get_range(self):
        sample = Sample([4, 1, 3, 2, 5])
        self.assertEqual(sample.get_range(), 4)

    @given(st.lists(st.integers(min_value=0, max_value=100), min_size=1))
    def test_set_data_property(self, data):
        sample = Sample()
        sample.set_data(data)
        self.assertEqual(sample.get_data(), data)

    @given(st.integers(min_value=1, max_value=100), st.lists(st.integers(min_value=0, max_value=100), min_size=1))
    def test_set_sample_property(self, n, sample_data):
        sample = Sample()
        sample.set_sample(n, sample_data)
        self.assertEqual(sample.get_sample(), (n, sample_data))

if __name__ == '__main__':
    cov.stop()
    cov.save()
    cov.html_report(directory='coverage_report')
    unittest.main()
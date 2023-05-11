import unittest
from unittest.mock import patch
import coverage
from hypothesis import given
from hypothesis.strategies import floats
from classes import Weather, temperature_converter


# Create and configure the coverage object
cov = coverage.Coverage()
cov.start()

class WeatherTest(unittest.TestCase):
    def setUp(self):
        self.weather = Weather(25, "Sunny", 60, 28)

    def test_get_temperature(self):
        self.assertEqual(self.weather.get_temperature(), 25)

    def test_set_temperature(self):
        self.weather.set_temperature(30)
        self.assertEqual(self.weather.get_temperature(), 30)

    def test_get_description(self):
        self.assertEqual(self.weather.get_description(), "Sunny")

    def test_set_description(self):
        self.weather.set_description("Cloudy")
        self.assertEqual(self.weather.get_description(), "Cloudy")

    def test_get_humidity(self):
        self.assertEqual(self.weather.get_humidity(), 60)

    def test_set_humidity(self):
        self.weather.set_humidity(70)
        self.assertEqual(self.weather.get_humidity(), 70)

    def test_get_feels_like(self):
        self.assertEqual(self.weather.get_feels_like(), 28)

    def test_set_feels_like(self):
        self.weather.set_feels_like(30)
        self.assertEqual(self.weather.get_feels_like(), 30)


class TemperatureConverterTest(unittest.TestCase):
    def setUp(self):
        self.temp_converter = temperature_converter(300)

    @given(floats(min_value=-1000, max_value=1000))
    def test_kelvin_to_cels_fahr(self, temp_k):
        self.temp_converter.set_temp_k(temp_k)
        celsius, fahrenheit = self.temp_converter.kelvin_to_cels_fahr()

        expected_celsius = temp_k - 273.15
        expected_fahrenheit = expected_celsius * (9 / 5) + 32

        self.assertAlmostEqual(celsius, expected_celsius, places=2)
        self.assertAlmostEqual(fahrenheit, expected_fahrenheit, places=2)


if __name__ == "__main__":
    # Stop coverage and generate the coverage report
    cov.stop()
    cov.save()
    cov.html_report(directory="coverage_report")

    # Run the tests
    unittest.main()
class Weather:
    def __init__(self, temperature, description, humidity, feels_like):
        self._temperature = temperature
        self._description = description
        self._humidity = humidity
        self._feels_like = feels_like

    def get_temperature(self):
        return self._temperature

    def set_temperature(self, temperature):
        self._temperature = temperature

    def get_description(self):
        return self._description

    def set_description(self, description):
        self._description = description
    
    def get_humidity(self):
        return self._humidity

    def set_humidity(self, humidity):
        self._humidity = humidity

    def get_feels_like(self):
        return self._feels_like

    def set_feels_like(self, feels_like):
        self._feels_like = feels_like


class temperature_converter:
    def __init__(self, temp_k):
        self._temp_k = temp_k

    def get_temp_k(self):
        return self._temp_k

    def set_temp_k(self, temp_k):
        self._temp_k = temp_k

    def kelvin_to_cels_fahr(self):
        celsius = self._temp_k - 273.15
        fahrenheit = celsius * (9/5) + 32
        return celsius, fahrenheit

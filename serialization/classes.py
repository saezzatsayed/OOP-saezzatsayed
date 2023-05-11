class Weather:
    def __init__(self, temperature, description):
        self._temperature = temperature
        self._description = description

    def get_temperature(self):
        return self._temperature

    def set_temperature(self, temperature):
        self._temperature = temperature

    def get_description(self):
        return self._description

    def set_description(self, description):
        self._description = description

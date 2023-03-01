class Temperature:
    min_temperature = 0
    max_temperature = 1000

    def __ini__(self, kelvin):
        self.kelvin = kelvin
    
    @classmethod
    def update_min_temperature(cls, kelvin):
        if Temperature.min_temperature < Temperature.max_temperature:
            Temperature.min_temperature = kelvin

    @classmethod
    def update_max_temperature(cls, kelvin):
        Temperature.max_temperature = kelvin

t1 = Temperature(260)
Temperature.update_max_temperature(270)
Temperature.update_min_temperature(680)

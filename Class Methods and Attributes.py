class Temperature:
    min_temperature = 0
    max_temperature = 1000
    
    def __init__(self, kelvin):
        if kelvin < self.min_temperature or kelvin > self.max_temperature:
            raise Exception("Invalid temperature.")
        self.kelvin = kelvin
    
    @classmethod
    def update_min_temperature(cls, kelvin):
        if cls.kelvin < cls.max_temperature:
            Temperature.min_temperature = cls.kelvin
        raise Exception("Invalid temperature.")

    @classmethod
    def update_max_temperature(cls, kelvin):
        cls.max_temperature = cls.kelvin


t1 = Temperature(260)



    
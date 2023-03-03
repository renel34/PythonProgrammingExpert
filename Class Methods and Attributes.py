class Temperature:
    min_temperature = 0
    max_temperature = 1000

    def __init__(self, kelvin):
        self.kelvin = kelvin
    
    @classmethod
    def update_min_temperature(cls, kelvin):
        if kelvin > cls.min_temperature and kelvin < cls.max_temperature:
            print(cls.min_temperature)
            if kelvin > cls.min_temperature:
                raise ValueError("Invalid temperature.")
            cls.min_temperature = kelvin
        
    @classmethod
    def update_max_temperature(cls, kelvin):
        if kelvin > cls.min_temperature and kelvin < cls.max_temperature:
            print(cls.max_temperature)
            if kelvin > cls.max_temperature:
                raise ValueError("Invalid temperature.")
            cls.max_temperature = kelvin
            print(cls.max_temperature)

t1 = Temperature(260)
Temperature.update_max_temperature(270)
Temperature.update_min_temperature(680)

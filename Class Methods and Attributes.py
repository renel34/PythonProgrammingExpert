class Temperature:
    min_temperature = 0
    max_temperature = 1000
    kelvin = 0

    def __init__(self, kelvin):
        self.kelvin = kelvin
        print(f"min = {self.min_temperature} max = {self.max_temperature}")
        if self.kelvin < Temperature.min_temperature or self.kelvin > Temperature.max_temperature:
            raise ValueError("Invalid Temperature.")
        
    @classmethod
    def update_min_temperature(cls, kelvin):
        cls.min_temperature = kelvin
        print(f"min = {cls.min_temperature} max = {cls.max_temperature}")
        if kelvin > cls.max_temperature:
            raise Exception("Invalid temperature.")
        print(f"min = {cls.min_temperature} max={cls.max_temperature}")
            

    @classmethod
    def update_max_temperature(cls, kelvin):
        cls.max_temperature = kelvin
        print(f"min = {cls.min_temperature} max = {cls.max_temperature}")
        

t1 = Temperature(260)
Temperature.update_max_temperature(270)
Temperature.update_min_temperature(680)
t2 = Temperature(280)
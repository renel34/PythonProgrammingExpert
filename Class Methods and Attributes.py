class Temperature:
    min_temperature = 0
    max_temperature = 1000
    kelvin = 0

    def __init__(self, kelvin):
        self.kelvin = kelvin
        
    @classmethod
    def update_min_temperature(cls, kelvin):
        print(f"min_temperature = {cls.min_temperature} and max_temperature = {cls.max_temperature}")
        print(kelvin)
        if kelvin > cls.min_temperature and kelvin < cls.max_temperature:
            if kelvin < cls.max_temperature:
                cls.min_temperature = kelvin
        raise Exception("Invalid temperature.")
           

    @classmethod
    def update_max_temperature(cls, kelvin):
        #print(f"min = {cls.min_temperature}  max = {cls.max_temperature}")
        if kelvin > cls.min_temperature and kelvin < cls.max_temperature:
            #print(F"{kelvin} is between {cls.min_temperature} and {cls.max_temperature}")
            cls.max_temperature = kelvin
            #print(f"min = {cls.min_temperature}  max = {cls.max_temperature}")
        

t1 = Temperature(260)
Temperature.update_max_temperature(270)
Temperature.update_min_temperature(680)

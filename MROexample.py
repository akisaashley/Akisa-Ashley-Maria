class Electric:
    def engine_type(self):
        return "Electric Motor"

class Hybrid:
    def engine_type(self):
        return "Hybrid Engine"

class Vehicle(Electric, Hybrid):
    pass

v = Vehicle()
print(v.engine_type())             
print(Vehicle.__mro__)           

r = range(30)
print(type(r))
print(type(10))
print(type('a'))
print(type('to evaluate'))


class Car:
    pass


class Truck(Car):
    pass


c = Car()
t = Truck()
print(type(c))
print(type(t))
print(type(c) == type(t))
print(isinstance(c, Car))
print(isinstance(t, Car))  # Takes inheritance

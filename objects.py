import array  # package
import math  # package
from math import ceil, asin  # mehtods

print("WHAT IS OBJECT")

print(type("Hello"))
print(type(98))
print(type(True))
print(type(array))
print(type(math))

result = math.ceil(97.7)
print(result)

result1 = ceil(98.7)
print(result1)


print("=====Error Handling syste ==========")
car_dict = dict(name="Toyota", year=2026, ev=True)

try:
    print("Passed here")
    a = car_dict.speed
    result = car_dict['year']
    print("Result:", result)
except KeyError as err:
    print("No origin state property found:", err)
except AttributeError as err:
    print("No speed attribute found:", err)
else:
    print("Executed withour errors")
finally:
    print("Final clothing logic")

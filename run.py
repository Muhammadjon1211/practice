# Dunder (double underscore) __builtin__, __init__ (ichki qurilishi mehanizmlari)
message = "Python: Everything is Object"
print(message)

result = type(message)
print("result:", result)

'''
In Python, there are builtin tools:
(1) TYPES > int float str list dict
(2) FUNCTION > print() len() input() type()
(3) CONSTANTS > True False None 
'''
print(dir(__builtins__))

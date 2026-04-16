'''
FUNTIONS
(1) define and call
(2) parameter and argiment
(3) keyword & default arguments
(4) scope
'''

print("=========defone And call==========")
# build in funciton > print() type()
# function - reusable block of code!
# Instead of block {} in java we use indentation


# DEFINE
def greet(a):
    print(f"Welcome back, {a}")


def greeting(b):
    print("greeting is executed")
    return f"Hello {b}"


# CALL
result1 = greet("John")
print("result1:", result1)  # void

result2 = greeting("Justin")
print("result2:", result2)


print("=========KEYWORDS & DEFAULT arguments==========")


def give_greet(name, age=22):
    print("give_greet is executed")
    return f"Hi {name.upper()} you are {age} years old."


result3 = give_greet("justin", age=28)
print("result3:", result3)

result4 = give_greet("john")
print("result4:", result4)

print("=========Scope==========")

b = 100


def calculate(a):
    c = a * b
    print(f"c value is:", c)


calculate(5)

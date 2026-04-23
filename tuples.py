print("=== What is tuple vs list")
# Java array => Pythonda List

numbs = [3, 5, 1, 2]
letter = list("Hello world")

fruits = ["apple", "lemon", "banana", "kiwi"]
print("before fruits:", fruits)

fruits[2] = 'melon'
print("after fruits:", fruits)

# tuple
animals = ("dog", "cat", "bear", "tiger")
tuple_obj = ("MIT", 110, True, None)
print(animals[0])
# animals[0] = "Lion"

# try avoid this
# people = "Andrew", "John"
# animals = "dog",

print("=== Unpacking arguemnts ===")

groups = ['MIT', "FLEXY", "DEVEX", "MG"]
(x, y, *z) = groups
print(f"thex: {x}, yhe y: {y}")
print(f"the z: {z}")

# args > tuple


def calculate(*args):
    print(f"*args > {args}")
    total = 1
    for x in args:
        total *= x
    print(f"the total value: {total}")
    return total


calculate(1, 7, 2, 3)
print(0, 2, 300)
print(2, 9)

# **kwargs > dictionary

# unpacking dictionary


def introduce(**kwargs):
    print(f"the type(**kwargs) value: {type(kwargs)}")
    print(f"Hi, I am {kwargs["name"]} and I am {kwargs['age']} years old!")


introduce(name="Justin", age=25)
introduce(name="Shawn", age=30, single=True)


def greating(*args, **kwargs):
    print("*args >", args)
    print("*kwargs >", kwargs)


greating("hi", True, 10, name='John', age=22)

print("== ZIP ===")
tuple1 = (1, 2, 3, 4)
tuple2 = ('a', 'b', 'c')

zipped = zip(tuple1, tuple2)
result = list(zipped)
print(result)

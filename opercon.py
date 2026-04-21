print("===Operators===")
a = 19
b = 5

result = a // b
left = a % b
print(f"the result: {result}, and the left: {left}")

a += 100
print("a:", a)

print("b**2:", b**2)
print("b**3:", b**3)

print("="*10)

c = dict(name="John", age=22)
d = dict(name="John", age=22)
e = c

print("c==d", c == d)  # only values are compared
print(id(c), id(d))

print("c is d:", c is d)
print("c is e:", c is e)

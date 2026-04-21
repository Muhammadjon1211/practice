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

print("=== Conditional ===")
x = 15

if x > 50:
    print("Case A")
elif x > 10:
    print("Case B")
else:
    print("Case C")

print('-'*10)

print("=== Logical Operators ===")
age = 20
# person = None
# if age > 16:
#     person = "adult"
# else:
#     person = 'child'

# print(person)

# Ternary Operator
person = "adult" if age > 18 else "minor"
print("person:", person)

is_student = True
is_admin = False
is_guest = True
is_parent = False

if not is_student:
    print("Welcome here, student")
elif is_admin:
    print("Please go to this office")
elif is_guest or is_parent:
    print("Waiting room is over there")
else:
    print("Other cases")

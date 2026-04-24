print("=== List ===")
# literal
person = {'name': "Justin", "age": 25}
people = ("Andrew", "John", "Michael")
groups = ["MIT", "FLEXY", "DEVEX", "MG"]
for team in groups:
    print(team)

# constructor
letters = list("Hello world")
print(f"the letters: {letters} and size: {len(letters)}")

print("================")
fruits = ['apple', 'orange', 'kiwi', 'watermelon']

a = fruits[0]
b = fruits[0:2]
c = fruits[::3]
d = fruits[::-1]

print("a:", a)
print("b:", b)
print("c:", c)
print("d:", d)

print("================")
print("=== List methos ===")
# methods: appendd(), insert(), pop(), remove(), clear(), sort(), index()
letters = ["a", "b", "d"]

letters.append("c")  # add begind mutable
print(f"append(): {letters}")

letters.insert(0, "z")  # add front mutable
print(f"insert(): {letters}")

size = len(letters) - 1
result1 = letters.pop(size)  # pop behind
print(f"pop(): {result1} and letters: {letters}")

result2 = letters.pop(0)  # pop front
print(f"result2: {result2}")

print("================")

animals = ['dog', 'cat', 'capybara', 'fish', 'lion']
print(animals)

animals.remove("lion")
print("remove:", animals)

del animals[2:4]  # mutablr
print("del:", animals)

exist = animals.index("cat")
print("index:", exist)

animals.clear()
print("clear:", animals)

try:
    exist = animals.index("cat")
    print("index:", exist)
except ValueError as err:
    print("Not in index")

print("================")
numbers = [2, 20, 12, 8, 57]
numbers.sort()
print("sort default:", numbers)

numbers.sort(reverse=True)
print("reverse:", numbers)

# immutable > sorted funstion
nums = [1, 32, 21, 12, 4, 5, 100]
new_nums = sorted(nums)
print("sorted:", new_nums)

print("=== Lambda Functions ===")
# lambda is small anonym function


def calculate(x, y): return x*y


result = calculate(3, 5)
print(result)

people = [
    ("Robert", 20),
    ("Steve", 19),
    ("Joseph", 23),
    ("Michael", 30),
    ("Ali", 18)
]

people.sort()
print("people(1)", people)

people.sort(key=lambda person: person[1])
print("people lambda", people)


print("=== enumerate, map, filter ===")
# enumerate for index & value
animals = ['dog', 'cat']
for element in enumerate(animals):
    print("element:", element)

for index, value in enumerate(animals):
    print(f"the index: {index} and value: {value}")

# dictinories
car_obj = dict(brand='ferrari', year=2025)
result = car_obj.items()
for key, value in car_obj.items():
    print(f"the index: {key} and value: {value}")

print("===============")
cars = [
    ('Ferrari', 78),
    ("Toyota", 87),
    ("Audi", 116),
    ("BMW", 109),
    ("Pagani", 33)
]

result1 = map(lambda car: car[0], cars)
print(f"result through lambda, {list(result1)}")

print("===============")
# filter
result_filter = filter(lambda car: car[1] > 80, cars)
print(f"result filter, {list(result_filter)}")

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

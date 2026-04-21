print("=== for operator ===")
# iterable objects > string dict tuple list range map filter

text = "MIT"
numbs = [10, 2, 5, 9]
car_obj = dict(brand="Ferrari", year=2025)
range_obj = range(5)

for letter in text:
    print(f"the letter: {letter}")

print('------')
for num in numbs:
    print(f"the number: {num}")

print('------')
for x in range_obj:
    print(f"the element: {x}")

for key in car_obj:
    print(f"the key: {key} => value: {car_obj.get(key)}")

print("================")
for x in range(1, 20, 5):
    print(f"the x: {x}")

print("=== break/else ===")
for x in range(1, 20, 5):
    print(f"the x: {x}")
    if x > 10:
        print("Reached break")
        break
else:
    print("Looped successfully")

print("=== while operator ===")
numb = 40
while numb > 0:
    numb -= 10
    print(f"the number equals to  {numb}")

print("=--=======")
count = 0
while True:
    count += 1
    x = int(input("Find number "))

    if x == 41:
        print(f"You found the number in {count} steps")
        break
    else:
        print("Wrong, please find again")

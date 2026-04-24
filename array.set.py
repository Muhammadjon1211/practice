from array import array

print("=== Array ===")
numbers = array("i", [1, 4, 5, 2, 3])  # only integers
numbers.append(100)
numbers.insert(0, 14)
print("numbers(2):", numbers)

numbers.remove(5)
numbers.pop()
print("numbers(3):", numbers)

del numbers[0:2]
print("numbers(4):", numbers)

print("=== Set ===")
# set uniqie collection without keeping order
new_numbers = array("i", [1, 5, 4, 5, 1, 2, 3])
numbers_set = set(new_numbers)
print(numbers_set)

numbers_set.add(200)
print("add():", numbers_set)

numbers_set.add(5)
print(numbers_set)

print("=== Specefic operators ===")
# | & - ^
a = {10, 20, 30}
b = {20, 40}
result1 = a | b  # union
result2 = a & b  # intersection
result3 = a - b  # difference
result4 = a ^ b  # symmetric difference takrorlanmaydigan qiymat
print(result1)
print(result2)
print("result3:", result3)
print("result4:", result4)

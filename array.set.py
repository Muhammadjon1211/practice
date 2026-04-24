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

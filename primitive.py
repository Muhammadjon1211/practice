print("==================")
# Pythonda Variable bu referencening nomlanishi, reference bu hotiradagi manzilga qaratilgan object


count = 100
count_type = type(count)
print(f"the count: {count} and type {count_type}")

result1 = count.bit_count()  # method
result2 = count.numerator  # state
print(result1, result2)


print("=========string=========")
# METHODS: upper() lower() title() find() replace()
course = "AI Python fullstack"
result = type(course)
print(f"The type of course: {result}")

result = course.title()
print(f"The type of course: {result}")

result3 = course.upper()
print(f"The type of course: {result3}")

result4 = course.lower()
print(f"The type of course: {result4}")

result5 = course.replace("fullstack", "mastery")
print(f"The type of course: {result5}")

result6 = course.find("fullstack")
print(f"The type of course: {result6}")

print(result)

print("=========boolean=========")
# fucnitons > type() input() bool() int() str()
y = input("Enter a value: ")
print("Y value is:", y)

result7 = y.isnumeric()
print(f"The input value is numeric: {result7}")

# TRUTHY & FALSY values
# TRUTHY > True 10, -100, "srtring"
# FALSY > False: False 0 "" None

test_falsy = "" or None or False or 0 or 100
print("The FALSY:", bool(test_falsy))

test_truthy = "JOHN"
print("The FALSY:", bool(test_truthy))

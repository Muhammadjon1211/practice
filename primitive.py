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

print("ITERABLE OBJECTS & RANGE")
# string, dict, tupe, list, range, map, filter

range_obj = range(3)
print("range_obj:", range_obj)

for letter in "MIT":
    print("The lette is:", letter)

for ele in range_obj:
    print("ele:", ele)

print("DICTIONARY")
# DICT or JASON object
person = {
    "name": "John",
    "age": 22,
    "single": True
}

person_dict = dict(name="Justin", age=29, single=False)

print(person)
print(person_dict)

# method: get()
# name = person_dict['name']
name = person_dict.get("name")
hobby = person_dict.get("hobby")
balance = person_dict.get("balance", 0)
print(f"The name is {name}, hobby is {hobby}, and the balance is {balance}")

del person_dict['single']
for key in person_dict:
    print(f"The key: {key}, the value: {person_dict.get(key)}")

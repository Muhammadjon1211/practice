print("=== What is comprehesion? ===")
# Comprehension acts like spread operator

'''Comprehension syntax:
    a) *iterable
    b) <expresssion> for item in interable
    c) <expresssion> for item in interable <condition>
'''

numbers = [2, 4, 3, 6, 1]
list_numbers = [*numbers]  # a version
print(list_numbers)
print(numbers is list_numbers)
print(id(numbers), id(list_numbers))


# person = ("Stieve", 18)
people = [("Robert", 20), ("Steve", 18), ("Joseph", 24)]
people_name = [person[0] for person in people]
print(people_name)

people_name = [person[0] for person in people if person[1] > 18]
print(people_name)

cars = [
    ('Ferrari', 78),
    ("Toyota", 87),
    ("Audi", 116),
    ("BMW", 109),
    ("Pagani", 33)
]

list_car = [car[0] for car in cars if car[1] > 80]
print(list_car)

print("=== Set and Dict comprehension ===")
nums = [2, 4, 3, 6, 1, 7, 4, 3]
set_nums = {*nums}
print(set_nums)

dict_list = {person[0]: person[1] for person in people}
print(dict_list)

dict_list2 = {person[0]: person[1] for person in people if person[1] > 20}
print(dict_list2)

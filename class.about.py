print("WHAT IS CLASS")


class Person():
    # state
    message = "class state property"

    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"{self.name} says: How are you")

    def say_age(self):
        print(f"{self.name} is {self.age} years old")

    @classmethod
    def explain(cls):
        print("Static method property executed")


person1 = Person("John", 22)
person2 = Person("Justin", 29)
person3 = Person("Nade", 28)

# ordinary state property
print(person1.name)

# ordinary method
person2.introduce()
person3.say_age()


print("=== ordinary and static properties ===")
# static state
new_message = Person.message
print(new_message)

# static method
Person.explain()


print("=== special methods ===")


class Car():
    description = "The class makes cars"

    # constructor (__init__ -> initializer)
    def __new__(cls, *args):
        print("*__new__*")
        return super().__new__(cls)

    def __init__(self, name, year):
        self.name = name
        self.year = year

    def start_engine(self):
        print(f"{self.name} stars engine")

    def stop_engine(self):
        print(f"{self.name} stops engine")

    def __str__(self):
        return f"The car name: {self.name} was manufactured in {self.year}"

    def __call__(self):
        print("Object executed as function")
        return True


my_car = Car("Toyota", 2015)
my_car.start_engine()
my_car.stop_engine()
print(my_car)

print("-------")
your_car = Car("Tesla", 2025)
print(your_car)
response = your_car()
print(response)

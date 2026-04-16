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

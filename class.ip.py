print("==Inheritance===")
# Parent > Child


class Animal:
    description = "THe class is parent for animals"

    def __init__(self, voice):
        self._status = "animal is alive"
        self.voice = voice

    def make_voice(self):
        print(f"The animal can make voice {self.voice}")


class Dog(Animal):
    def __init__(self, name, sound, voice):
        super().__init__(voice)
        self.name = name
        self.sound = sound

    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def protect(self):
        print("Yes, I can protect you!")

    def make_voice(self):
        print(f"The {self.name} can {self.sound}")


class Cat(Animal):
    # state

    # constructor
    def __init__(self, name, sound, voice):
        super().__init__(voice)
        self.name = name
        self.sound = sound

    # method
    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def play(self):
        pass


class Fish(Animal):
    # state

    # constructor
    def __init__(self, name, sound, voice):
        super().__init__(voice)
        self.name = name
        self.sound = sound

    # method
    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def swin(self):
        print("Yes, I can swim!")


dog = Dog("Rex", "wow", True)
cat = Cat("Tom", "myeow", True)
fish = Fish("Nemo", "zzz", False)

dog.introduce()
cat.introduce()
print('==============')
dog.make_voice()
cat.make_voice()
fish.make_voice()

print(Animal.description)
print(Dog.description)

print(dog.voice, fish.voice)
print('status:', dog._status)


print("===POLYMORPHISM===")
dog.make_voice()
fish.make_voice()

print("===")
# fish > Fish > Animal > object
a = isinstance(fish, Fish)
b = isinstance(fish, Fish)
c = isinstance(fish, object)
d = isinstance("MIT", object)
print(a, b, c, d)


data = issubclass(Fish, Animal)
data1 = issubclass(Animal, object)
print(data, data1)

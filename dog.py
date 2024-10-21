import random

class Dog:
    created = 0

    def __init__(self, name, breed, age = 0, height = 10):
        print("Dog class called")
        self.name = name
        self.age = age
        self.breed = breed
        self.height = height
        self.sound = ""
        Dog.created = Dog.created + 1

    def __str__(self):
        return f"{self.name}"

    def increase_age(self, years = 1):
        self.age = self.age + years

    def set_sound(self, sound):
        self.sound = sound

    def bark(self, count):
        print(f"{self.name} is about to bark")
        for i in range(count):
            print(self.sound)

print(Dog.created)

dog = Dog("Musti", "Labrador", 4)
print(Dog.created)
dog2 = Dog("Fluffy", "Shetland Pony")
print(Dog.created)

dog2.set_sound("yip")
dog2.bark(3)

print(f"Dog name: {dog.name}, age {dog.age}, breed {dog.breed}, height: {dog.height}")
print(f"Dog2 name: {dog2.name}, age {dog2.age}, breed {dog2.breed}, height: {dog.height}")
dog.increase_age()
print(f"Dog name: {dog.name}, age {dog.age}, breed {dog.breed}")
print(f"Dog2 name: {dog2.name}, age {dog2.age}, breed {dog2.breed}")

#dog2 = Dog()
#print(f"Dog name: {dog2.name}")

kennel = [dog, dog2]

dog3 = Dog("Dog 3", "Dog", 2)
kennel.append(dog3)

for i in range(10_000):
    dog = Dog(f"Dog{i}", "Shetland pony", i)
    kennel.append(dog)

print(kennel[1].name)

for dog in kennel:
    dog.increase_age(random.randint(0, 15))
    print(f"Dog {dog.name} (aged {dog.age}) is in kennel")

print("--------")

for dog in kennel:
    dog.increase_age(random.randint(0, 15))
    print(f"Dog {dog.name} (aged {dog.age}) is in kennel")


print(f"Dogs created: {Dog.created}")

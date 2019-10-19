class Animal:
    def eat(self):
        print("eating...")

class Dog(Animal):
    def bark(self):
        print("barking...")

class Cat(Animal):
    def meow(self):
        print("meowing...")

c = Cat()
c.meow()

d = Dog()
d.bark()
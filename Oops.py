# ==================================================
# 1. CLASS AND OBJECT - Student Example
# ==================================================

class Student:
    name = "Shivam"

s1 = Student()
print(s1.name)


# ==================================================
# 2. CLASS AND OBJECT - Car Example
# ==================================================

class Car:
    color = "Red"

c1 = Car()
print(c1.color)


# ==================================================
# 3. ENCAPSULATION - Student Age Example
# ==================================================

class Student:
    def __init__(self):
        self.__age = 21

    def get_age(self):
        return self.__age

s1 = Student()
print(s1.get_age())


# ==================================================
# 4. ENCAPSULATION - Bank Balance Example
# ==================================================

class Bank:
    def __init__(self):
        self.__balance = 1000

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

b = Bank()
b.deposit(500)

print(b.get_balance())


# ==================================================
# 5. INHERITANCE - Animal and Dog Example
# ==================================================

class Animal:
    def eat(self):
        print("Animal eats")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()
d.eat()
d.bark()


# ==================================================
# 6. INHERITANCE - Vehicle and Bike Example
# ==================================================

class Vehicle:
    def start(self):
        print("Vehicle starts")

class Bike(Vehicle):
    def ride(self):
        print("Bike is riding")

b = Bike()
b.start()
b.ride()


# ==================================================
# 7. POLYMORPHISM - Method Overriding Example
# ==================================================

class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

d = Dog()
d.sound()


# ==================================================
# 8. POLYMORPHISM - Dog and Cat Example
# ==================================================

class Dog:
    def sound(self):
        print("Dog barks")

class Cat:
    def sound(self):
        print("Cat meows")

for animal in [Dog(), Cat()]:
    animal.sound()


# ==================================================
# 9. ABSTRACTION - Animal and Dog Example
# ==================================================

from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Dog barks")

d = Dog()
d.sound()


# ==================================================
# 10. ABSTRACTION - Vehicle and Car Example
# ==================================================

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car starts")

c = Car()
c.start()
# 1. Abstraction – Hiding internal complexity, only exposing essentials

from abc import ABC, abstractmethod

# Abstract Base Class
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass  # Abstract method, must be implemented in child classes

# Concrete Class
class Dog(Animal):
    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

# Usage
d = Dog()
d.make_sound()  # Output: Woof!

c = Cat()
c.make_sound()  # Output: Meow!

# 2. Inheritance – One class (child) inherits from another (parent)

# Parent class
class Vehicle:
    def start(self):
        print("Engine started")

# Child class inheriting Vehicle
class Car(Vehicle):
    def drive(self):
        print("Car is driving")

# Usage
c = Car()
c.start()    # Inherited method from Vehicle
c.drive()    # Child class method


# 3. Polymorphism – Same method name behaves differently for different classes

class Bird:
    def fly(self):
        print("Bird is flying")

class Airplane:
    def fly(self):
        print("Airplane is flying")

# Common interface
def lift_off(entity):
    entity.fly()  # Polymorphic call

# Usage
b = Bird()
a = Airplane()

lift_off(b)  # Output: Bird is flying
lift_off(a)  # Output: Airplane is flying

# 4. Encapsulation – Hiding data using private variables

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private variable using __

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance  # Accessing private variable safely

# Usage
account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # Output: 1500

# print(account.__balance)   # ❌ This will raise an error (private)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

print(person1.name, person1.age)
print(person2.name, person2.age)


class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(self.name, "says Woof!")

dog1 = Dog("Buddy")
dog1.bark()


dog1.name = "Max"
print(dog1.name)


class Company:
    company_name = "TechCorp"

    def __init__(self, employee_name):
        self.employee_name = employee_name

emp1 = Company("Alice")
emp2 = Company("Bob")

print(Company.company_name)
print(emp1.employee_name)
print(emp2.employee_name)


class Student:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Student name:", self.name)

student1 = Student("John")
student1.display()


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

user1 = User("admin", "1234")
del user1.password


class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):
        print(self.name, "says Woof!")

class Cat(Animal):
    def speak(self):
        print(self.name, "says Meow!")

dog = Dog("Buddy")
cat = Cat("Whiskers")

dog.speak()
cat.speak()


class Bird:
    def fly(self):
        print("Bird is flying")

class Airplane:
    def fly(self):
        print("Airplane is flying")

def make_it_fly(entity):
    entity.fly()

bird = Bird()
plane = Airplane()
make_it_fly(bird)
make_it_fly(plane)

from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started")

car = Car()
car.start_engine()

class Parent:
    def show(self):
        print("Parent method")

class Child(Parent):
    def show(self):
        print("Child method")

child = Child()
child.show()

class Engine:
    def start(self):
        print("Engine started")

class Wheels:
    def roll(self):
        print("Wheels rolling")

class Car(Engine, Wheels):
    pass

my_car = Car()
my_car.start()
my_car.roll()

class Book:
    def __init__(self, title):
        self.title = title

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        for book in self.books:
            print(book.title)

library = Library()
library.add_book(Book("Python Basics"))
library.add_book(Book("Advanced OOP"))
library.show_books()
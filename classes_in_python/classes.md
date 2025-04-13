# Python Classes

This document provides an overview of different types of classes in Python, including their implementation and best practices.

## Table of Contents

1. [Basic Classes and Instances](#1-basic-classes-and-instances)
2. [Class Variables](#2-class-variables)
3. [Instance Attributes](#3-instance-attributes)
4. [Class Methods](#4-class-methods)
5. [Static Methods](#5-static-methods)
6. [Dataclasses](#6-dataclasses)
7. [Abstract Base Classes](#7-abstract-base-classes)
8. [Inheritance](#8-inheritance)
9. [Polymorphism](#9-polymorphism)
10. [Encapsulation](#10-encapsulation)
11. [Magic Methods](#11-magic-methods)
12. [Property Decorator](#12-property-decorator)
13. [Iterator Class](#13-iterator-class)
14. [Best Practices](#best-practices)

## 1. Basic Classes and Instances

A class is a blueprint to create instances. Instances are created based on a blueprint called a class. A class defines attributes as data and methods as functions associated with it.

```python
class Employee:
    def __init__(self, first, last, pay):
        self.first = first  # instance variable
        self.last = last    # instance variable
        self.pay = pay

# Creating instances
emp1 = Employee("Arthur", "Klark", 1000)
emp2 = Employee("Brigitte", "Klark", 2000)
```

## 2. Class Variables

Class variables are variables that are shared between all instances of a class. They are declared within the class but outside of any class methods.

```python
class Employee:
    raise_amount = 1.04  # class variable
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

emp1 = Employee('Arthur', 'Klark', 1000)
emp1.apply_raise()
print(emp1.pay)  # Output: 1040
```

## 3. Instance Attributes

Instance attributes are unique to each instance of a class. They are defined within methods, typically in the `__init__` method.

```python
class Employee:
    def __init__(self, first, last, pay):
        self.first = first  # instance attribute
        self.last = last    # instance attribute
        self.pay = pay      # instance attribute
        self.email = f"{first}.{last}@company.com"  # instance attribute

# Each instance has its own copy of these attributes
emp1 = Employee("Arthur", "Klark", 1000)
emp2 = Employee("Brigitte", "Klark", 2000)
```

## 4. Class Methods

Class methods receive the class as the first argument instead of an instance. They are defined using the @classmethod decorator.

```python
class Employee:
    raise_amount = 1.04
    
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount
        
    @classmethod
    def from_string(cls, emp_str):
        """Create an employee from a string in format 'first-last-pay'"""
        first, last, pay = emp_str.split('-')
        return cls(first, last, int(pay))

# Usage
Employee.set_raise_amount(1.07)
emp_str = 'Johnny-Mnemonic-100000'
new_emp = Employee.from_string(emp_str)
```

## 5. Static Methods

Static methods don't automatically receive any argument and only take the arguments that are explicitly provided. They are defined using the @staticmethod decorator.

```python
import datetime

class Employee:
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

# Usage
my_date = datetime.date(2017, 10, 22)
print(Employee.is_workday(my_date))  # Output: False
```

## 6. Dataclasses

Dataclasses are a decorator and functions for automatically adding generated special methods to classes. They reduce boilerplate code.

```python
from dataclasses import dataclass

@dataclass
class Employee:
    first: str
    last: str
    pay: int
    email: str = None

    def __post_init__(self):
        if self.email is None:
            self.email = f"{self.first}.{self.last}@company.com"

# Usage
emp = Employee("Arthur", "Klark", 1000)
print(emp)  # Automatically generates __repr__
```

## 7. Abstract Base Classes

Abstract Base Classes (ABCs) define a blueprint for other classes. They can't be instantiated and require subclasses to implement abstract methods.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)
```

## 8. Inheritance

Inheritance allows a new class to be based on an existing class, inheriting its attributes and methods.

```python
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

class Developer(Employee):
    raise_amount = 1.10  # Override class variable
    
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        self.employees = employees if employees is not None else []
    
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def print_emp(self):
        for emp in self.employees:
            print(f"-> {emp.fullname()}")

# Usage
dev1 = Developer('Arthur', 'Klark', 1000, 'Python')
mng1 = Manager('Robert', 'Doyle', 500, [dev1])
```

## 9. Polymorphism

Polymorphism allows objects of different classes to be treated as objects of a common superclass.

```python
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

def animal_sound(animal):
    print(animal.speak())

# Usage
dog = Dog()
cat = Cat()
animal_sound(dog)  # Output: Woof!
animal_sound(cat)  # Output: Meow!
```

## 10. Encapsulation

Encapsulation is the bundling of data and methods that operate on that data within a single unit, and restricting access to some of the object's components.

```python
class BankAccount:
    def __init__(self, balance):
        self._balance = balance  # Protected attribute
        self.__pin = "1234"      # Private attribute

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def withdraw(self, amount, pin):
        if pin == self.__pin and amount <= self._balance:
            self._balance -= amount
            return True
        return False
```

## 11. Magic Methods

Magic methods (or dunder methods) are special methods that start and end with double underscores. They allow you to define how objects behave with built-in operations.

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __len__(self):
        return 2

# Usage
v1 = Vector(2, 4)
v2 = Vector(1, 3)
v3 = v1 + v2
print(v3)  # Output: Vector(3, 7)
```

## 12. Property Decorator

The @property decorator makes a method accessible as an attribute instead of a method.

```python
class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
    
    @property
    def fullname(self):
        return f"{self.first} {self.last}"

# Usage
emp = Employee('Arthur', 'Klark')
print(emp.fullname)  # Note: no parentheses needed
```

## 13. Iterator Class

An iterator class implements the __iter__ and __next__ methods to provide a sequence of values.

```python
class SquaresIterator:
    def __init__(self, max_root_value):
        self.max_root_value = max_root_value
        self.current_root_value = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current_root_value >= self.max_root_value:
            raise StopIteration
        square_value = self.current_root_value ** 2
        self.current_root_value += 1
        return square_value

# Usage
for num in SquaresIterator(5):
    print(num)  # Output: 0, 1, 4, 9, 16
```

## Best Practices

1. Use type hints for better code clarity
2. Validate inputs to prevent errors
3. Use proper docstrings for documentation
4. Handle exceptions appropriately
5. Use inheritance when appropriate
6. Keep methods focused and single-purpose
7. Use property decorators for computed attributes
8. Implement proper iterator protocols when needed
9. Use dataclasses to reduce boilerplate code
10. Implement proper encapsulation for data protection
11. Use abstract base classes for interface definition
12. Leverage polymorphism for flexible code design
13. Implement appropriate magic methods for custom behavior

## Requirements

- Python 3.6+
- No external dependencies required (except for dataclasses which are built-in since Python 3.7) 
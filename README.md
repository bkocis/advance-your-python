### Examples of using OOP in python, and other python handy-dandys
___

## On object-oriented programming in python

This repository contains a small number of examples of beginner level topics on the theme of classes in python.

Contents:
- [classes](https://bkocis.github.io/advance-your-python/classes_in_pythoon/classes)
  - [class variables](https://bkocis.github.io/advance-your-python/classes_in_pythoon/classes#Class_variables)
  - [instance attributes](https://bkocis.github.io/advance-your-python/classes_in_pythoon/classes#Classes_and_instances)
  - [class methods](https://bkocis.github.io/advance-your-python/classes_in_pythoon/classes#Classmethods)
  - [static methods](https://bkocis.github.io/advance-your-python/classes_in_pythoon/classes#Staticmethods)
  - [dataclasses](https://bkocis.github.io/advance-your-python/classes_in_pythoon/dataclasses)
  - [abstract base classes](https://bkocis.github.io/advance-your-python/classes_in_pythoon/abstract_classes)
- [inheritance](https://bkocis.github.io/advance-your-python/classes_in_pythoon/classes#Inharitance)
- [polymorphism](https://bkocis.github.io/advance-your-python/classes_in_pythoon/polymorphism)
- [encapsulation](https://bkocis.github.io/advance-your-python/classes_in_pythoon/encapsulation)
- [magic methods](https://bkocis.github.io/advance-your-python/classes_in_pythoon/magic_methods)
- [decorators](https://bkocis.github.io/advance-your-python/classes_in_pythoon/decorators)
- [generators](https://bkocis.github.io/advance-your-python/classes_in_pythoon/generators)
- [context managers](https://bkocis.github.io/advance-your-python/classes_in_pythoon/context_managers)
- [iterators](https://bkocis.github.io/advance-your-python/classes_in_pythoon/iterators)


Readings:

[5-python-tricks](https://towardsdatascience.com/5-python-tricks-that-distinguish-senior-developers-from-juniors-826d57ab3940)

[How-to-level-up-by-learning-from-professionals](https://medium.com/towards-data-science/how-to-level-up-your-python-skills-by-learning-from-these-professionals-3e906b83f355)

[10-code-examples-AoC](https://medium.com/techtofreedom/10-remarkable-python-oop-tips-that-will-optimize-your-code-significantly-a47e4103b44d)


Comparison of list comprehansions and `map()` functions: 

[comparing-list-comprehensions-vs-built-in-functions-in-python-which-is-better](https://towardsdatascience.com/comparing-list-comprehensions-vs-built-in-functions-in-python-which-is-better-1e2c9646fafe)


```python
# given a list, the map function can transform it
l = ['1', '2']

def square_me(x):
    return x**2 + 2 

list(map(square_me, map(int, l)))

Out: [3, 6]

```

[should-you-use-getters-and-setters-in-python](https://python.plainenglish.io/should-you-use-getters-and-setters-in-python-d4db9a892878)

[Protocols-in-python](https://godatadriven.com/blog/protocols-in-python-why-you-need-them/)

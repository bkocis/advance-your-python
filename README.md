### Small example for using OOP in python
___

## On object-oriented programming in python

This repository contains a small number of examples of beginner level topics on the theme of classes in python.

https://towardsdatascience.com/5-python-tricks-that-distinguish-senior-developers-from-juniors-826d57ab3940
https://medium.com/towards-data-science/how-to-level-up-your-python-skills-by-learning-from-these-professionals-3e906b83f355
https://medium.com/techtofreedom/10-remarkable-python-oop-tips-that-will-optimize-your-code-significantly-a47e4103b44d


```python
# given a list, the map funciton can transform it
l = ['1', '2']

def square_me(x):
    return x**2 

list(map(square_me, map(int, l)))

Out[16]: [3, 6]

```
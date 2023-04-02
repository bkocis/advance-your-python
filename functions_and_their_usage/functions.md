
Comparison of list comprehensions and `map()` functions: 

```python
# given a list, the map function can transform it
l = ['1', '2']

def square_me(x):
    return x**2 + 2 

list(map(square_me, map(int, l)))

Out: [3, 6]

```

## Functions

### `map`
Simpe example of the `map()` function that simply applies a function to each element of a list 

```python
# given a list, the map function can transform it
l = ['1', '2']

def square_me(x):
    return x**2 + 2 

list(map(square_me, map(int, l)))

Out: [3, 6]

```

### `map` with `filter`


### `map` with `reduce`


### `*args` and `**kwargs`



```python


def boo(a,b,**kwargs):
    if kwargs:
        c = kwargs['c']
        return a*b*c
    return a*b
# the **kwargs can be any dict, with specified keys and values
k = {'c':3}
# passing it as **kwargs
boo(1,2,**k)
# it is also optional
boo(1,2)

# *args is simply a tuple, which can be unpacked in the function for use
def goo(*args):
    return sum([i for i in args])

```

Using "/" and "*" in the function definition to specify the parameters that can be passed as positional or keyword arguments

```pyhton
def f(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)
```
This page follows the examples from the [official documentation on expressions in python](https://docs.python.org/3/reference/expressions.html)

and 

[PEP 572](https://peps.python.org/pep-0572/)

### Some expressions

#### `Assignement expressions`

```python
ORDERS = [{"id": "one"}, {"id": "two"}] 
order_id = "one"
if order := [order for order in ORDERS if order['id'] == order_id]:
    print(f"Order id {order_id} found!")
```

The above code is equivalent to checking the property of the list (len) to see if it is empty or not

```python
order_id = 'one'
order = [order for order in ORDERS if order['id']==order_id]
if len(order) > 0:
    print(f"Order id {order_id} found!")
```

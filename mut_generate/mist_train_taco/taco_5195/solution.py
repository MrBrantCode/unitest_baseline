"""
QUESTION:
You will be given an array which lists the current inventory of stock in your store and another array which lists the new inventory being delivered to your store today.

Your task is to write a function that returns the updated list of your current inventory **in alphabetical order**.

## Example

```python
cur_stock = [(25, 'HTC'), (1000, 'Nokia'), (50, 'Samsung'), (33, 'Sony'), (10, 'Apple')]
new_stock = [(5, 'LG'), (10, 'Sony'), (4, 'Samsung'), (5, 'Apple')]

update_inventory(cur_stock, new_stock)  ==>
[(15, 'Apple'), (25, 'HTC'), (5, 'LG'), (1000, 'Nokia'), (54, 'Samsung'), (43, 'Sony')]
```

___

*Kata inspired by the FreeCodeCamp's 'Inventory Update' algorithm.*
"""

from collections import defaultdict

def update_inventory(cur_stock, new_stock):
    answer = defaultdict(int)
    for (stock, item) in cur_stock + new_stock:
        answer[item] += stock
    return [(answer[item], item) for item in sorted(answer)]
"""
QUESTION:
----
Vampire Numbers
----

Our loose definition of [Vampire Numbers](http://en.wikipedia.org/wiki/Vampire_number) can be described as follows:

```python
6 * 21 = 126
# 6 and 21 would be valid 'fangs' for a vampire number as the 
# digits 6, 1, and 2 are present in both the product and multiplicands

10 * 11 = 110
# 110 is not a vampire number since there are three 1's in the
# multiplicands, but only two 1's in the product
```

Create a function that can receive two 'fangs' and determine if the product of the two is a valid vampire number.
"""

def is_vampire_number(x: int, y: int) -> bool:
    """
    Determines if the product of two numbers (x and y) is a valid vampire number.

    A vampire number is defined such that the digits of the product of x and y
    are exactly the same as the digits of x and y combined, regardless of order.

    Parameters:
    x (int): The first potential fang.
    y (int): The second potential fang.

    Returns:
    bool: True if the product of x and y is a valid vampire number, otherwise False.
    """
    return sorted(str(x * y)) == sorted(str(x) + str(y))
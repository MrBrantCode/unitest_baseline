"""
QUESTION:
Create a `Vector` class with `x` and a `y` attributes that represent component magnitudes in the x and y directions.

Your vectors should handle vector additon with an `.add()` method that takes a second vector as an argument and returns a new vector equal to the sum of the vector you call `.add()` on and the vector you pass in.

For example:

```python
>>> a = Vector(3, 4)
>>> a.x
3
>>> a.y
4
>>> b = Vector(1, 2)
>>> c = a.add(b)
>>> c.x
4
>>> c.y
6
```

Adding vectors when you have their components is easy: just add the two x components together and the two y components together to get the x and y components for the vector sum.
"""

def add_vectors(vector1, vector2):
    """
    Adds two vectors represented as tuples or lists of two elements each.

    Parameters:
    vector1 (tuple or list): The first vector, e.g., (x1, y1).
    vector2 (tuple or list): The second vector, e.g., (x2, y2).

    Returns:
    tuple: The resultant vector after addition, e.g., (x_sum, y_sum).
    """
    x_sum = vector1[0] + vector2[0]
    y_sum = vector1[1] + vector2[1]
    return (x_sum, y_sum)
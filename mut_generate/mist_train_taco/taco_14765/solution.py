"""
QUESTION:
Write a function
```python
alternate_sort(l)
```
that combines the elements of an array by sorting the elements ascending by their **absolute value** and outputs negative and non-negative integers alternatingly (starting with the negative value, if any).

E.g.
```python
alternate_sort([5, -42, 2, -3, -4, 8, -9,]) == [-3, 2, -4, 5, -9, 8, -42]
alternate_sort([5, -42, 2, -3, -4, 8, 9]) == [-3, 2, -4, 5, -42, 8, 9]
alternate_sort([5, 2, -3, -4, 8, -9]) == [-3, 2, -4, 5, -9, 8]
alternate_sort([5, 2, 9, 3, 8, 4]) == [2, 3, 4, 5, 8, 9]
```
"""

from itertools import chain, zip_longest

def alternate_sort(l):
    # Sort the list by absolute value
    l = sorted(l, key=abs)
    
    # Separate the list into positive and negative numbers
    positives = [n for n in l if n >= 0]
    negatives = [n for n in l if n < 0]
    
    # Alternate between negative and positive numbers
    result = [n for n in chain(*zip_longest(negatives, positives)) if n is not None]
    
    return result
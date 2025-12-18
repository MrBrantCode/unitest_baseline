"""
QUESTION:
Write a program that outputs the `n` largest elements from a list.

Example:
```python
largest(2, [7,6,5,4,3,2,1])
# => [6,7]
```
"""

def get_n_largest_elements(n, xs):
    return sorted(xs)[-n:]
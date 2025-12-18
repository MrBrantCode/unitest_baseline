"""
QUESTION:
Write a function that flattens an `Array` of `Array` objects into a flat `Array`.  Your function must only do one level of flattening.

```python
flatten [1,2,3] # => [1,2,3]
flatten [[1,2,3],["a","b","c"],[1,2,3]]  # => [1,2,3,"a","b","c",1,2,3]
flatten [[[1,2,3]]] # => [[1,2,3]]
```
"""

def flatten_one_level(lst):
    """
    Flattens a list of lists into a flat list, performing only one level of flattening.

    Parameters:
    lst (list): The input list of lists to be flattened.

    Returns:
    list: A flat list with one level of flattening applied.
    """
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(item)
        else:
            result.append(item)
    return result
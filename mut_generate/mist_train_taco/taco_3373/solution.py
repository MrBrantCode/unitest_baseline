"""
QUESTION:
Is every value in the array an array?

This should only test the second array dimension of the array. The values of the nested arrays don't have to be arrays. 

Examples:

```python
[[1],[2]] => true
['1','2'] => false
[{1:1},{2:2}] => false
```
"""

def are_all_elements_arrays(arr):
    """
    Check if every value in the array is an array (list).

    Parameters:
    arr (list): A list of elements to be checked.

    Returns:
    bool: True if all elements in the array are lists, False otherwise.
    """
    return all(isinstance(el, list) for el in arr)
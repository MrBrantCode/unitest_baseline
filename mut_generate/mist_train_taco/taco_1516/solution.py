"""
QUESTION:
Write a function with the signature shown below:
```python
def is_int_array(arr):
    return True
```
* returns `true  / True`  if every element in an array is an integer or a float with no decimals.
* returns `true  / True`  if array is empty.
* returns `false / False` for every other input.
"""

def is_int_array(arr):
    """
    Check if every element in the array is an integer or a float with no decimals, or if the array is empty.

    Parameters:
    arr (list): The input array to be checked.

    Returns:
    bool: True if the conditions are met, False otherwise.
    """
    return isinstance(arr, list) and all((isinstance(x, (int, float)) and x == int(x) for x in arr))